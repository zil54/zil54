let socket = null;

function analyze() {
  const fen = document.getElementById("fen").value;
  const evalBox = document.getElementById("eval");
  evalBox.innerText = "";

  socket = new WebSocket("ws://localhost:8000/ws/analyze");

  socket.onopen = () => {
    socket.send(fen);
  };

  socket.onmessage = (event) => {
    const line = event.data;
    if (line.includes("pv")) {
      evalBox.innerText += line + "\n";
    }
  };

  socket.onerror = (err) => {
    evalBox.innerText += "WebSocket error: " + err.message;
  };

  socket.onclose = () => {
    evalBox.innerText += "\n[Analysis stopped]";
  };
}

function stopAnalysis() {
  if (socket) {
    socket.close();
    socket = null;
  }
}
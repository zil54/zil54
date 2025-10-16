fetch("http://localhost:8000/svg", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ fen: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" })
})
fetch("http://localhost:8000/svg", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ fen: this.fen })
})
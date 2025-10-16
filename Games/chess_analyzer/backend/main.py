from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import Response, HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from svg import generate_board_svg
from engine import run_stockfish
from stockfish_session import StockfishSession
import uvicorn
import asyncio
import os

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static assets
app.mount("/static", StaticFiles(directory="static"), name="static")

# Persistent Stockfish session
base_dir = os.path.dirname(os.path.dirname(__file__))  # chess_analyzer/
stockfish_path = os.path.join(base_dir, "stockfish", "sf.exe")
stockfish = StockfishSession(stockfish_path)

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse("static/index.html")

@app.get("/index.html")
async def serve_index():
    return FileResponse("static/index.html")

@app.post("/svg")
async def svg(request: Request):
    data = await request.json()
    fen = data.get("fen", "")
    svg_markup = generate_board_svg(fen)
    return Response(content=svg_markup, media_type="image/svg+xml")

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    fen = data.get("fen", "")
    try:
        result = run_stockfish(fen, lines=3)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.websocket("/ws/analyze")
async def analyze_ws(websocket: WebSocket):
    await websocket.accept()
    fen = await websocket.receive_text()

    stockfish.send("uci")
    stockfish.send(f"position fen {fen}")
    stockfish.send("go infinite")

    try:
        async for line in stream_stockfish():
            if "pv" in line:
                await websocket.send_text(line)
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")
        await websocket.close()

async def stream_stockfish():
    loop = asyncio.get_event_loop()
    for line in stockfish.read_lines():
        yield line
        await asyncio.sleep(0.1)  # throttle output slightly

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


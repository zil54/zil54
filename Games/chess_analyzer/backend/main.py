from fastapi import FastAPI, Request, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response, HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from Games.chess_analyzer.backend.svg.svg import generate_board_svg
from Games.chess_analyzer.engine.engine import run_stockfish
from Games.chess_analyzer.engine.stockfish_session import StockfishSession
import uvicorn
import asyncio
import os
from logs.logger import logger

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
logger.info("Serving static assets for the app")

# Persistent Stockfish session
base_dir = os.path.dirname(os.path.dirname(__file__))  # chess_analyzer/
stockfish_path = os.path.join(base_dir, "engine", "sf.exe")
if not os.path.exists(stockfish_path):
    logger.error(f"Stockfish binary not found at: {stockfish_path}")
    raise FileNotFoundError(f"Missing Stockfish binary at: {stockfish_path}")
stockfish = StockfishSession(stockfish_path)
logger.info("Connected to Stockfish")


@app.post("/svg")
async def svg(request: Request):
    data = await request.json()
    fen = data.get("fen", "")
    logger.info("Received FEN for SVG: %s", fen)

    try:
        svg_markup = generate_board_svg(fen)
        if not svg_markup or "<svg" not in svg_markup:
            logger.error("SVG generation failed or malformed")
            return Response(content="SVG generation failed", status_code=500)

        logger.info("SVG generated successfully")
        return Response(content=svg_markup, media_type="image/svg+xml")

    except Exception as e:
        logger.exception("SVG generation error")
        return Response(content="SVG generation error", status_code=500)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    fen = data.get("fen", "")
    try:
        result = run_stockfish(fen, lines=3)
        return result
        if result is not None:
            logger.info("Analyze generated successfully")
        else:
            logger.error("Analyze generated but didn't produce result")
    except Exception as e:
        return {"error": str(e)}
        logger.exception("SF Run produced an error")

@app.websocket("/ws/analyze")
async def analyze_ws(websocket: WebSocket):
    await websocket.accept()
    fen = await websocket.receive_text()

    logger.info("Sending uci....")
    stockfish.send("uci")
    logger.info("Send 3 lines")
    stockfish.send("setoption name MultiPV value 3")
    logger.info("Sending fen....")
    stockfish.send(f"position fen {fen}")
    logger.info("Sending go infinite...")
    stockfish.send("go infinite")

    try:
        async for line in stream_stockfish():
            if "pv" in line:
                await websocket.send_text(line)
                logger.info("Displaying infinite was successful")
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")
        logger.error(str(e))
        await websocket.close()

async def stream_stockfish():
    loop = asyncio.get_event_loop()
    while True:
        line = await loop.run_in_executor(None, stockfish.process.stdout.readline)
        if line:
            line = line.strip()
            logger.debug("Streaming line from Stockfish: %s", line)
            yield line
        await asyncio.sleep(0.1)  # throttle output slightly

app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="frontend")
if __name__ == "__main__":
    uvicorn.run("Games.chess_analyzer.backend.main:app", host="127.0.0.1", port=8000, reload=True)


from Games.chess_analyzer.backend.db.core import SessionLocal
from Games.chess_analyzer.backend.db.models import SessionAnalysis, AnalysisLines

# -------------------------
# Session management
# -------------------------

async def create_session(fen: str) -> SessionAnalysis:
    """Create a new analysis session with given FEN."""
    async with SessionLocal() as s:
        obj = SessionAnalysis(fen=fen, status="created")
        s.add(obj)
        await s.commit()
        await s.refresh(obj)
        return obj


async def get_session(session_id):
    """Fetch a session by ID."""
    async with SessionLocal() as s:
        return await s.get(SessionAnalysis, session_id)


# -------------------------
# Analysis lines
# -------------------------

async def upsert_line(session_id, depth: int, multipv: int, line: str) -> None:
    """Insert or update an analysis line for a given session/depth/multipv."""
    async with SessionLocal() as s:
        obj = await s.get(
            AnalysisLines,
            {"session_id": session_id, "depth": depth, "multipv": multipv}
        )
        if obj:
            obj.line = line
        else:
            obj = AnalysisLines(
                session_id=session_id,
                depth=depth,
                multipv=multipv,
                line=line,
            )
            s.add(obj)
        await s.commit()


async def get_latest_lines(session_id):
    """Return the max depth and all lines at that depth for a session."""
    async with SessionLocal() as s:
        # Get the maximum depth for this session
        result = await s.execute(
            """
            SELECT MAX(depth) FROM analysis_lines
            WHERE session_id = :sid
            """,
            {"sid": session_id},
        )
        row = result.first()
        if not row or row[0] is None:
            return None, []

        max_depth = row[0]

        # Fetch all lines at that depth
        lines = await s.execute(
            """
            SELECT * FROM analysis_lines
            WHERE session_id = :sid AND depth = :d
            ORDER BY multipv
            """,
            {"sid": session_id, "d": max_depth},
        )
        return max_depth, lines.fetchall()
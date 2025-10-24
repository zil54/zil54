from Games.chess_analyzer.backend.db.repo import create_session, get_session, upsert_line, get_latest_lines
from Games.chess_analyzer.testing.helper1_move_numbering import add_move_numbers
import pytest

@pytest.mark.asyncio
async def test_create_and_fetch_session():
    fen = "r1bqkbnr/pppppppp/n7/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    session = await create_session(fen)

    assert session.id is not None
    assert session.fen == fen
    assert session.status == "created"

    fetched = await get_session(session.id)
    assert fetched is not None
    assert fetched.id == session.id
    assert fetched.fen == fen

@pytest.mark.asyncio
async def test_upsert_and_latest_lines_with_numbering():
    # 1. Create a new session
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    session = await create_session(fen)

    # 2. Insert a PV line (raw moves)
    raw_line = "e4 e5 Nf3 Nc6"
    numbered_line = add_move_numbers(raw_line)

    await upsert_line(session.id, depth=10, multipv=1, line=numbered_line)

    # 3. Fetch latest lines
    depth, rows = await get_latest_lines(session.id)

    assert depth == 10
    assert len(rows) == 1

    # 4. Assert numbering is present
    stored_line = rows[0].line
    assert stored_line.startswith("1.")        # must start with move number
    assert "2." in stored_line                 # second move number should appear
    assert "e4" in stored_line and "Nc6" in stored_line

    raw_line = "e5 Nf3 Nc6"
    numbered_line = add_move_numbers(raw_line, black_to_move=True)
    assert numbered_line.startswith("1...")  # Black to move


import pytest

from routes.progress.router import add_progress
from routes.types import ProgressRequest


@pytest.mark.parametrize(
    "user_id, progress, expected",
    [
        ("1100", "progress1", 200),
        ("1101", "progress1", 400),
        ("1101", "progress3", 200),
        ("1102", "progress1", 400),
    ],
)
async def test_add_progress(user_id, progress, expected) -> None:
    """Тест на добавление прогресса"""
    result = await add_progress(user_id=user_id, body=ProgressRequest(progress_name=progress))
    assert result.status_code == expected

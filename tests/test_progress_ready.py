import pytest

from routes.progress.ready.router import ready_progress
from routes.types import ProgressRequest


@pytest.mark.parametrize(
    "user_id, progress_name, status_code",
    [
        ("1101", "progress1", 200),
        ("1101", "progress2", 400),
        ("1102", "progress1", 200),
        ("1102", "progress2", 400),
    ]
)
async def test_ready_progress(user_id: str, progress_name: str, status_code:int) -> None:
    """Тест на отметку сегодняшнего дня"""
    result = await ready_progress(user_id=user_id, body=ProgressRequest(progress_name=progress_name))
    assert result.status_code == status_code

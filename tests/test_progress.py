import pytest

from routes.progress.router import add_progress
from routes.types import ProgressRequest


@pytest.mark.parametrize(
    'user_id, progress_name, status_code',
    [
        ('1100', 'progress1', 200),
        ('1101', 'progress1', 400),
        ('1101', 'progress3', 200),
        ('1102', 'progress1', 400),
    ],
)
async def test_add_progress(user_id: str, progress_name: str, status_code: int) -> None:
    '''Тест на добавление прогресса'''
    result = await add_progress(user_id=user_id, body=ProgressRequest(progress_name=progress_name))
    assert result.status_code == status_code

import pytest


from ..routes.progress.router import add_progress


@pytest.mark.parametrize(
    'user_id, progress, expected',
    [
        ('1100', 'progress1', 200),
        ('1101', 'progress1', 300),
        ('1101', 'progress3', 200),
        ('1102', 'progress1', 300),
    ],
)

def test_add_progress(user_id, progress, expected) -> None:
    assert add_progress(user_id=user_id, progress_name=progress)[]

import pytest


@pytest.fixture
def request_add_progress():
    return {'user_id': '1101', 'progress': 'progress1'}

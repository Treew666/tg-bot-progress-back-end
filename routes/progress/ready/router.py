from fastapi import APIRouter

from functions.processing_json import (
    add_ready_user_progress,
    is_progress_in_user_id,
    is_user_id_in_vault,
)
from routes.types import Answer, ProgressRequest

router = APIRouter()


@router.post("/{user_id}")
async def ready_progress(user_id: str, body: ProgressRequest) -> Answer:
    """Добавление отметки (дату) выполнения прогресса"""
    progress_name = body.progress_name
    if not is_user_id_in_vault(user_id=user_id):
        return Answer(status_code=400, info=f"the user, {user_id}, not found")
    if not is_progress_in_user_id(user_id=user_id, progress_name=progress_name):
        return Answer(
            status_code=400, info=f"the user, {user_id}, has no progress, {progress_name}"
        )
    try:
        today = add_ready_user_progress(user_id=user_id, progress_name=progress_name)
        return Answer(status_code=200, info=f"successful add today date, {today}, in progress, {progress_name}, for user, {user_id}")
    except ValueError as valueError:
        return Answer(status_code=400, info=str(valueError))

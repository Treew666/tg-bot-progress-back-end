from fastapi import APIRouter

from functions.processing_json import add_progress_user, delete_progress_user, is_user_id_in_vault
from routes.types import Answer, ProgressRequest

router = APIRouter()


@router.post("/{user_id}")
async def add_progress(user_id: str, body: ProgressRequest) -> Answer:
    """Добавление прогресса"""
    progress_name = body.progress_name
    try:
        if is_user_id_in_vault(user_id=user_id):
            text_info = f"successful add progress, {progress_name}, for user, {user_id}"
        else:
            text_info = f"successful add user, {user_id}, and progress, {progress_name}"

        add_progress_user(user_id=user_id, progress_name=progress_name)
        return Answer(status_code=200, info=text_info)

    except ValueError:
        return Answer(
            status_code=400, info=f"the user, {user_id}, already has progress, {progress_name}"
        )


@router.delete("/{user_id}/{progress_name}")
async def delete_progress(user_id: str, progress_name: str) -> Answer:
    """Удаление прогресса"""
    if not is_user_id_in_vault(user_id=user_id):
        return Answer(status_code=400, info=f"the user, {user_id}, not found")
    try:
        delete_progress_user(user_id=user_id, progress_name=progress_name)
        return Answer(
            status_code=200,
            info=f"succesful delete progress, {progress_name}, for user, {user_id}",
        )
    except ValueError as valueError:
        return Answer(status_code=400, info=str(valueError))
        

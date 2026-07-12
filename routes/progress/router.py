from fastapi import APIRouter
from ..types import Answer, ProgressRequest
from functions.processing_json import is_user_id_in_vault, add_progress_user


router = APIRouter()


@router.post('/{user_id}')
async def add_progress(user_id: str, body: ProgressRequest) -> Answer:
    '''Добавление прогресса'''
    progress_name = body.progress_name
    try:
        if is_user_id_in_vault(user_id=user_id):
            text_info = f'successful add progress, {progress_name}, for user, {user_id}'
        else:
            text_info = f'successful add user, {user_id}, and progress, {progress_name}'
            
        add_progress_user(user_id=user_id, progress_name=progress_name)
        return Answer(
            status_code = 200,
            info = text_info
        )
        
    except ValueError:
        return Answer(
            status_code = 400,
            info = f'the user, {user_id}, already has progress, {progress_name}'
        )

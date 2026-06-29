from typing import Any
from fastapi import APIRouter
from ..types import answer
from functions.processing_json import is_user_id_in_vault


router = APIRouter()


from pydantic import BaseModel

class answer(BaseModel):
    status_code: int
    info: str

@router.post('/{user_id}')
async def add_progress(user_id: str, progress_name: str) -> answer:
    if is_user_id_in_vault(user_id=user_id):
        pass

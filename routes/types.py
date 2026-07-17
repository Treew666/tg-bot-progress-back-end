from pydantic import BaseModel


class Answer(BaseModel):
    status_code: int
    info: str


class ProgressRequest(BaseModel):
    progress_name: str

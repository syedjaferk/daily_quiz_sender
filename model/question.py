from pydantic import BaseModel
from typing import List


class Question(BaseModel):
    question: str
    options: List[str]
    correct_option_id: int
    explanation: str
    chat_id: str
    type: str
    is_anonymous: bool

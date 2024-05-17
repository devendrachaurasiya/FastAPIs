from pydantic import BaseModel
from typing import List

class InputLoad(BaseModel):
    batchid: str
    payload: List[List[int]]

class OutputResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: str
    completed_at: str
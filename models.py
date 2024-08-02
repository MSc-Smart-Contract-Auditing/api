from pydantic import BaseModel
from typing import List


class Contract(BaseModel):
    name: str
    ast: object
    source: str


class SubmitRequest(BaseModel):
    root: Contract
    dependencies: List[Contract]

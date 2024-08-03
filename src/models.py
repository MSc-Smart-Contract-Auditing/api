from pydantic import BaseModel
from typing import List, Dict


class Contract(BaseModel):
    name: str
    ast: object
    raw: str


class Function(BaseModel):
    id: int
    name: str
    source: str


class FunctionNode(BaseModel):
    func: Function
    invocations: List[int]


class WorkUnit(BaseModel):
    lookup: Dict[int, FunctionNode]
    mainIds: List[int]

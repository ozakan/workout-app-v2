from pydantic import BaseModel
from typing import List

# 入力（POST / PATCH 用）
class WorkoutBase(BaseModel):
    date: str


class SetResponse(BaseModel):
    id: int
    weight: int
    reps: int

    class Config:
        orm_mode = True


class ExerciseResponse(BaseModel):
    id: int
    name: str
    sets: List[SetResponse] = []

    class Config:
        orm_mode = True


class WorkoutResponse(BaseModel):
    id: int
    date: str
    exercises: List[ExerciseResponse] = []

    class Config:
        orm_mode = True


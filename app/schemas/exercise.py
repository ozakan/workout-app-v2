from pydantic import BaseModel

# 入力（POST, PATCH用）
class ExerciseBase(BaseModel):
    name: str

# 出力（レスポンス用）
class ExerciseResponse(ExerciseBase):
    id: int
    workout_id: int

    class Config:
        orm_mode = True

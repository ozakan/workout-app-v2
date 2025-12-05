from pydantic import BaseModel

# 入力（POST / PATCH 用）
class WorkoutBase(BaseModel):
    date: str

# 出力（レスポンス用）
class WorkoutResponse(WorkoutBase):
    id: int

    class Config:
        orm_mode = True

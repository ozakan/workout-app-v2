from pydantic import BaseModel

# 入力（POSTやPATCH）
class SetBase(BaseModel):
    weight: int
    reps: int

# 出力（レスポンス用）
class SetResponse(SetBase):
    id: int
    exercise_id: int

    class Config:
        orm_mode = True

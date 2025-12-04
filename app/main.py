from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from app.database import Base, engine, get_db
from app.models import Workout, Exercise, Set
from sqlalchemy.orm import Session
from fastapi import HTTPException

app = FastAPI()

# ① アプリ起動時に DB のテーブルを作成する
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


# ② 動作確認用：トップページ
@app.get("/")
def home():
    return {"message": "Workout App ORM version"}


# ③ Workout を作成（POST /workouts）
@app.post("/workouts")
def create_workout(date: str, db: Session = Depends(get_db)):
    workout = Workout(date=date)
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout


# ④ 特定の Workout を取得（GET /workouts/{date}）
@app.get("/workouts/{date}")
def get_workout(date: str, db: Session = Depends(get_db)):
    workout = (
        db.query(Workout)
        .filter(Workout.date == date)
        .first()
    )
    return workout


# ⑤ Exercise を追加（POST /workouts/{workout_id}/exercises）
@app.post("/workouts/{workout_id}/exercises")
def add_exercise(workout_id: int, name: str, db: Session = Depends(get_db)):
    exercise = Exercise(workout_id=workout_id, name=name)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


# ⑥ 特定 Workout の Exercise 一覧
@app.get("/workouts/{workout_id}/exercises")
def list_exercises(workout_id: int, db: Session = Depends(get_db)):
    exercises = (
        db.query(Exercise)
        .filter(Exercise.workout_id == workout_id)
        .all()
    )
    return exercises


# ⑦ Set を追加（POST /exercises/{exercise_id}/sets）
@app.post("/exercises/{exercise_id}/sets")
def add_set(exercise_id: int, weight: int, reps: int, db: Session = Depends(get_db)):
    new_set = Set(exercise_id=exercise_id, weight=weight, reps=reps)
    db.add(new_set)
    db.commit()
    db.refresh(new_set)
    return new_set


# ⑧ Exercise の Set 一覧
@app.get("/exercises/{exercise_id}/sets")
def list_sets(exercise_id: int, db: Session = Depends(get_db)):
    sets = (
        db.query(Set)
        .filter(Set.exercise_id == exercise_id)
        .all()
    )
    return sets

@app.patch("/exercises/{exercise_id}")
def update_exercise(exercise_id: int, name: str, db: Session = Depends(get_db)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")

    exercise.name = name
    db.commit()
    db.refresh(exercise)
    return exercise

@app.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")

    db.delete(exercise)
    db.commit()
    return {"message": "Exercise deleted"}

@app.patch("/sets/{set_id}")
def update_set(set_id: int, weight: int, reps: int, db: Session = Depends(get_db)):
    set_item = db.query(Set).filter(Set.id == set_id).first()
    if set_item is None:
        raise HTTPException(status_code=404, detail="Set not found")

    set_item.weight = weight
    set_item.reps = reps

    db.commit()
    db.refresh(set_item)
    return set_item

@app.delete("/sets/{set_id}")
def delete_set(set_id: int, db: Session = Depends(get_db)):
    set_item = db.query(Set).filter(Set.id == set_id).first()
    if set_item is None:
        raise HTTPException(status_code=404, detail="Set not found")

    db.delete(set_item)
    db.commit()
    return {"message": "Set deleted"}

@app.patch("/workouts/{workout_id}")
def update_workout(workout_id: int, date: str, db: Session = Depends(get_db)):
    workout = db.query(Workout).filter(Workout.id == workout_id).first()
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")

    workout.date = date
    db.commit()
    db.refresh(workout)
    return workout

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = db.query(Workout).filter(Workout.id == workout_id).first()
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")

    db.delete(workout)
    db.commit()
    return {"message": "Workout deleted"}

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database import init_db, get_connection
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def home():
    return {"message": "Workout App v2"}


@app.get("/workout/{date}")
def workout_page(request: Request, date: str):
    """
    指定された日付のトレーニングページを表示する
    """
    conn = get_connection()
    cur = conn.cursor()

    # その日の workout があるか確認（ない場合は作成）
    cur.execute("SELECT * FROM workouts WHERE date = ?", (date,))
    row = cur.fetchone()

    if row is None:
        # 新しいワークアウトを作成
        cur.execute("INSERT INTO workouts (date) VALUES (?)", (date,))
        conn.commit()
        workout_id = cur.lastrowid
    else:
        workout_id = row["id"]

    # この日の exercises を取得
    cur.execute("SELECT * FROM exercises WHERE workout_id = ?", (workout_id,))
    exercises = cur.fetchall()

    conn.close()

    return templates.TemplateResponse(
        "workout.html",
        {
            "request": request,
            "date": date,
            "workout_id": workout_id,
            "exercises": exercises
        }
    )

@app.get("/workout/{date}/add_exercise")
def add_exercise_form(request: Request, date: str):
    return templates.TemplateResponse(
        "add_exercise.html",
        {"request": request, "date": date}
    )

@app.post("/workout/{date}/add_exercise")
def add_exercise(request: Request, date: str, name: str = Form(...)):
    conn = get_connection()
    cur = conn.cursor()

    # workout_id を取得（なければ作る）
    cur.execute("SELECT id FROM workouts WHERE date = ?", (date,))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO workouts (date) VALUES (?)", (date,))
        conn.commit()
        workout_id = cur.lastrowid
    else:
        workout_id = row["id"]

    # exercises に INSERT
    cur.execute(
        "INSERT INTO exercises (workout_id, name) VALUES (?, ?)",
        (workout_id, name)
    )
    conn.commit()
    conn.close()

    return RedirectResponse(url=f"/workout/{date}", status_code=302)

@app.post("/workout/{date}/delete_exercise/{exercise_id}")
def delete_exercise(date: str, exercise_id: int):
    conn = get_connection()
    cur = conn.cursor()

    # まず、その exercise に紐づく sets を削除
    cur.execute("DELETE FROM sets WHERE exercise_id = ?", (exercise_id,))
    conn.commit()

    # 次に exercises を削除
    cur.execute("DELETE FROM exercises WHERE id = ?", (exercise_id,))
    conn.commit()

    conn.close()

    # 元のページにリダイレクト
    return RedirectResponse(url=f"/workout/{date}", status_code=302)


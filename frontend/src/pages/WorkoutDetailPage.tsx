import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

/* ===== 型定義 ===== */

type Set = {
  id: number;
  weight: number;
  reps: number;
};

type Exercise = {
  id: number;
  name: string;
  sets: Set[];
};

type Workout = {
  id: number;
  date: string;
  exercises: Exercise[];
};

/* ===== コンポーネント ===== */

function WorkoutDetailPage() {
  const { date } = useParams();
  const [workout, setWorkout] = useState<Workout | null>(null);

  useEffect(() => {
    if (!date) return;

    fetch(`http://127.0.0.1:8000/workouts/${date}`)
      .then(res => res.json())
      .then(data => setWorkout(data))
      .catch(err => {
        console.error(err);
        setWorkout(null);
      });
  }, [date]);

  if (!workout) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Workout Detail</h1>
      <p>日付: {workout.date}</p>

      <h2>Exercises</h2>

      {workout.exercises.length === 0 && (
        <p>種目がまだ登録されていません</p>
      )}

      {workout.exercises.map(ex => (
        <div key={ex.id} style={{ marginBottom: "24px" }}>
          <h3>{ex.name}</h3>

          {ex.sets.length === 0 && (
            <p>セットがまだ登録されていません</p>
          )}

          <ul>
            {ex.sets.map(s => (
              <li key={s.id}>
                {s.weight}kg × {s.reps}回
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default WorkoutDetailPage;

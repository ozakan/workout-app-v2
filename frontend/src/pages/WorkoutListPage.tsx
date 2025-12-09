import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

type Workout = {
  id: number;
  date: string;
};

function WorkoutListPage() {
  const [workouts, setWorkouts] = useState<Workout[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/workouts")
      .then(res => res.json())
      .then(data => setWorkouts(data));
  }, []);

  return (
    <div>
      <h1>Workout List</h1>
      <ul>
        {workouts.map(w => (
          <li key={w.id}>
            <Link to={`/workout/${w.date}`}>{w.date}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default WorkoutListPage;

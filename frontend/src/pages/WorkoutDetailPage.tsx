import { useParams } from "react-router-dom";

function WorkoutDetailPage() {
  const { date } = useParams();

  return (
    <div>
      <h1>Workout Detail</h1>
      <p>日付: {date}</p>
    </div>
  );
}

export default WorkoutDetailPage;

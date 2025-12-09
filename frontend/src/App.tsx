import { Routes, Route } from "react-router-dom";
import WorkoutListPage from "./pages/WorkoutListPage";
import WorkoutDetailPage from "./pages/WorkoutDetailPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<WorkoutListPage />} />
      <Route path="/workout/:date" element={<WorkoutDetailPage />} />
    </Routes>
  );
}

export default App;

// static/js/api.js
function getToken() {
  return localStorage.getItem("token");
}

export async function requestJson(url, options = {}) {
  const headers = new Headers(options.headers || {});
  const token = getToken();
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const res = await fetch(url, { ...options, headers });
  const text = await res.text();

  if (!res.ok) {
    if (res.status === 401) {
      localStorage.removeItem("token");
      location.href = "/";
    }
    throw new Error(`HTTP ${res.status}: ${text}`);
  }

  if (!text) return null;
  return JSON.parse(text);
}


export async function getWorkouts() {
  const data = await requestJson("/workouts/");
  const items = Array.isArray(data) ? data : (data?.items ?? data?.workouts ?? []);
  return items;
}

export async function addWorkout(date) {
  return await requestJson("/workouts/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ date }),
  });
}

export async function deleteWorkout(workoutId) {
  return await requestJson(`/workouts/${workoutId}`, {
    method: "DELETE",
  });
}

export async function getWorkoutById(workoutId) {
  return await requestJson(`/workouts/${workoutId}`);
}

export async function deleteSet(setId) {
  return await requestJson(`/sets/${setId}`, { method: "DELETE" });
}

export async function deleteExercise(exerciseId) {
  return await requestJson(`/exercises/${exerciseId}`, { method: "DELETE" });
}

export async function addExercise(workoutId, name) {
  return await requestJson(`/workouts/${workoutId}/exercises`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
}

export async function addSet(exerciseId, weight, reps) {
  return await requestJson(`/exercises/${exerciseId}/sets`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ weight, reps }),
  });
}

export async function updateSet(setId, weight, reps) {
  return await requestJson(`/sets/${setId}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ weight, reps }),
  });
}

export async function updateExercise(exerciseId, name) {
  return await requestJson(`/exercises/${exerciseId}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
}



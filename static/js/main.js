// static/js/main.js
console.log("main.js loaded");

import { initWorkoutsPage } from "./workouts.js";

document.addEventListener("DOMContentLoaded", () => {
  initWorkoutsPage();
});

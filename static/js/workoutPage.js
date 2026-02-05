import { getWorkoutById, deleteSet, deleteExercise, addExercise, addSet, updateSet, updateExercise } from "./api.js";

function getWorkoutIdFromQuery() {
  const params = new URLSearchParams(window.location.search);
  return params.get("workout_id");
}

function renderWorkout(workout) {
  // 日付
  document.getElementById("date").textContent = workout.date;

  const container = document.getElementById("exercises");
  container.innerHTML = "";

  workout.exercises.forEach((ex) => {
    const exDiv = document.createElement("div");

    // 種目名
    const titleRow = document.createElement("div");
    titleRow.style.margin = "8px 0";

    const nameInput = document.createElement("input");
    nameInput.type = "text";
    nameInput.value = ex.name;
    nameInput.style.width = "200px";

    const saveNameBtn = document.createElement("button");
    saveNameBtn.textContent = "種目名保存";
    saveNameBtn.style.marginLeft = "6px";

    const delExBtn = document.createElement("button");
    delExBtn.textContent = "種目削除";
    delExBtn.style.marginLeft = "6px";

    const titleMsg = document.createElement("span");
    titleMsg.style.marginLeft = "8px";

    saveNameBtn.addEventListener("click", async () => {
      titleMsg.textContent = "";
      const name = nameInput.value.trim();
      if (!name) {
        titleMsg.textContent = "種目名を入力してください";
        return;
      }

      try {
        await updateExercise(ex.id, name);
        titleMsg.textContent = "保存しました";
        await init();
      } catch (e) {
        titleMsg.textContent = "保存失敗: " + e.message;
      }
    });

    delExBtn.addEventListener("click", async () => {
      if (!confirm(`「${ex.name}」を削除しますか？`)) return;

      try {
        await deleteExercise(ex.id);
        await init();
      } catch (e) {
        alert("削除失敗: " + e.message);
      }
    });

    titleRow.appendChild(nameInput);
    titleRow.appendChild(saveNameBtn);
    titleRow.appendChild(delExBtn);
    titleRow.appendChild(titleMsg);

    exDiv.appendChild(titleRow);



    // セット一覧
    const ul = document.createElement("ul");
    ex.sets.forEach((s) => {
      const li = document.createElement("li");

      const wInput = document.createElement("input");
      wInput.type = "number";
      wInput.value = s.weight;
      wInput.style.width = "70px";

      const repsInput = document.createElement("input");
      repsInput.type = "number";
      repsInput.value = s.reps;
      repsInput.style.width = "70px";
      repsInput.style.marginLeft = "6px";

      const saveBtn = document.createElement("button");
      saveBtn.textContent = "保存";
      saveBtn.style.marginLeft = "6px";

      const delBtn = document.createElement("button");
      delBtn.textContent = "🗑";
      delBtn.style.marginLeft = "6px";

      const msg = document.createElement("span");
      msg.style.marginLeft = "8px";

      saveBtn.addEventListener("click", async () => {
        msg.textContent = "";
        const weight = Number(wInput.value);
        const reps = Number(repsInput.value);

        if (!Number.isFinite(weight) || !Number.isFinite(reps)) {
          msg.textContent = "数値を入力してください";
          return;
        }

        try {
          await updateSet(s.id, weight, reps);
          msg.textContent = "保存しました";
          await init();
        } catch (e) {
          msg.textContent = "保存失敗: " + e.message;
        }
      });

      delBtn.addEventListener("click", async () => {
        if (!confirm("このセットを削除しますか？")) return;

        try {
          await deleteSet(s.id);
          await init();
        } catch (e) {
          alert("削除失敗: " + e.message);
        }
      });

      li.appendChild(wInput);
      li.appendChild(repsInput);
      li.appendChild(saveBtn);
      li.appendChild(delBtn);
      li.appendChild(msg);

      ul.appendChild(li);
    });

    
    
    exDiv.appendChild(ul);
    // --- セット追加フォーム（weight/reps） ---
    const formRow = document.createElement("div");
    formRow.style.margin = "8px 0";

    const wInput = document.createElement("input");
    wInput.type = "number";
    wInput.placeholder = "重量";
    wInput.style.width = "80px";

    const repsInput = document.createElement("input");
    repsInput.type = "number";
    repsInput.placeholder = "回数";
    repsInput.style.width = "80px";
    repsInput.style.marginLeft = "6px";

    const addBtn = document.createElement("button");
    addBtn.textContent = "セット追加";
    addBtn.style.marginLeft = "6px";

    const msg = document.createElement("span");
    msg.style.marginLeft = "8px";

    addBtn.addEventListener("click", async () => {
      msg.textContent = "";

      const weight = Number(wInput.value);
      const reps = Number(repsInput.value);

      // 最低限のバリデーション
      if (!Number.isFinite(weight) || !Number.isFinite(reps)) {
        msg.textContent = "重量と回数を入力してください";
        return;
      }

      try {
        await addSet(ex.id, weight, reps);
        msg.textContent = "追加しました";
        wInput.value = "";
        repsInput.value = "";
        await init(); // 再取得→再描画
      } catch (e) {
        msg.textContent = "追加失敗: " + e.message;
      }
    });

    formRow.appendChild(wInput);
    formRow.appendChild(repsInput);
    formRow.appendChild(addBtn);
    formRow.appendChild(msg);
    exDiv.appendChild(formRow);
    container.appendChild(exDiv);
  });
}

async function init() {
  const workoutId = getWorkoutIdFromQuery();
  if (!workoutId) {
    alert("workout_id が指定されていません");
    return;
  }

  const msgEl = document.getElementById("msg");
  const inputEl = document.getElementById("new-ex-name");
  const addBtn = document.getElementById("add-ex");

  // 何度もinitが呼ばれるので、クリックを二重登録しないように一旦クリアしてから登録
  addBtn.onclick = async () => {
    msgEl.textContent = "";
    const name = inputEl.value.trim();

    if (!name) {
      msgEl.textContent = "種目名を入力してください";
      return;
    }

  try {
    await addExercise(workoutId, name);
    inputEl.value = "";
    msgEl.textContent = "追加しました";
    await init(); // 再取得→再描画
  } catch (e) {
    msgEl.textContent = "追加失敗: " + e.message;
  }
};


  try {
    const workout = await getWorkoutById(workoutId);
    console.log(workout);
    renderWorkout(workout);
  } catch (e) {
    alert("読み込み失敗: " + e.message);
  }
}

document.addEventListener("DOMContentLoaded", init);

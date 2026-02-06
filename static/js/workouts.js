// static/js/workouts.js
import { getWorkouts, addWorkout, deleteWorkout } from "./api.js";

function renderList(listEl, items, onDelete) {
  listEl.innerHTML = "";

  items.forEach((w) => {
    const li = document.createElement("li");

    const label = document.createElement("span");
    label.textContent = w.date; // ここはシンプルに
    li.appendChild(label);

    // ★ 追加：詳細へ遷移（idがあるときだけ）
    if (w.id != null) {
      li.style.cursor = "pointer";
      li.addEventListener("click", () => {
        location.href = `/static/workout.html?workout_id=${w.id}`;
      });
    }

    // idが無いと削除できないので、無い場合はボタンを出さない
    if (w.id != null) {
      const delBtn = document.createElement("button");
      delBtn.textContent = "削除";
      delBtn.style.marginLeft = "8px";

      delBtn.addEventListener("click", (e) => {
        e.stopPropagation(); // ★ 重要：削除クリックで詳細遷移しない
        onDelete(w.id);
      });
      li.appendChild(delBtn);
    }

    listEl.appendChild(li);
  });
}



export function initWorkoutsPage() {
  const listEl = document.getElementById("list");
  const addBtn = document.getElementById("add");
  const dateInput = document.getElementById("date");
  const msg = document.getElementById("msg");

  
  const logoutBtn = document.getElementById("logout");
  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      localStorage.removeItem("token");
      location.href = "/";
    });
  }


  async function loadWorkouts() {
    const items = await getWorkouts();
    console.log("workouts:", items);
    renderList(listEl, items, handleDelete);
  }

  loadWorkouts().catch((e) => {
    console.error(e);
    alert("Load failed: " + e.message);
  });

  addBtn.addEventListener("click", async () => {
    msg.textContent = "";

    const date = dateInput.value;
    if (!date) {
      msg.textContent = "日付を入力してください";
      return;
    }

    try {
      await addWorkout(date);
      msg.textContent = "追加しました";
      await loadWorkouts();
    } catch (e) {
      console.error(e);
      msg.textContent = "POST failed: " + e.message;
    }
  });

  async function handleDelete(id) {
    if (!confirm("このworkoutを削除しますか？")) return;

    msg.textContent = "";
    try {
      await deleteWorkout(id);
      msg.textContent = "削除しました";
      await loadWorkouts();
    } catch (e) {
      console.error(e);
      msg.textContent = "DELETE failed: " + e.message;
    }
  }

}


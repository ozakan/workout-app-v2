async function login(username, password) {
  const res = await fetch("/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const text = await res.text();
  if (!res.ok) {
    throw new Error(text);
  }

  const data = JSON.parse(text);
  localStorage.setItem("token", data.access_token);
}

const loginBtn = document.getElementById("login");
const msg = document.getElementById("msg");

loginBtn.addEventListener("click", async () => {
  msg.textContent = "";

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    await login(username, password);
    location.href = "/static/workouts.html";
  } catch (e) {
    msg.textContent = "ログイン失敗";
  }
});

async function register(username, password) {
  const res = await fetch("/auth/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const text = await res.text();
  if (!res.ok) {
    throw new Error(text);
  }

  return JSON.parse(text);
}

const registerBtn = document.getElementById("register");
const regMsg = document.getElementById("reg-msg");

registerBtn.addEventListener("click", async () => {
  regMsg.textContent = "";

  const username = document.getElementById("reg-username").value;
  const password = document.getElementById("reg-password").value;

  if (!username || !password) {
    regMsg.textContent = "ユーザー名とパスワードを入力してください";
    return;
  }

  try {
    await register(username, password);
    regMsg.textContent = "登録成功！ログインしてください";
  } catch (e) {
    regMsg.textContent = "登録失敗：" + e.message;
  }
});

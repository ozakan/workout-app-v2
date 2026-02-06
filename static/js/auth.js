
import { requestJson } from "./api.js"; // もしexportしてないなら、loginだけapi.jsに追加でもOK

export function setToken(token) {
  localStorage.setItem("token", token);
}

export function clearToken() {
  localStorage.removeItem("token");
}

export async function login(username, password) {
  const data = await requestJson("/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  localStorage.setItem("token", data.access_token);
  return data;
}

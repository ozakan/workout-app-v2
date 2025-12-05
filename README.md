# Workout App v2 (FastAPI + SQLAlchemy)

このアプリは、筋トレ内容（Workout / Exercise / Set）を管理する  
**REST API ベースの筋トレ記録アプリ**です。

現在はバックエンド API を中心に実装中で、  
フロントエンドは後から接続予定です。

---

## 🛠 技術スタック

- **FastAPI**
- **SQLAlchemy (ORM)**
- **SQLite**
- **Python 3.11**
- **Uvicorn**

---

## 📦 機能（現時点）

### ✔ Workout（1日分のトレーニング）
- `POST /workouts` : 新規作成
- `GET /workouts/{date}` : 取得
- `PATCH /workouts/{id}` : 日付の更新
- `DELETE /workouts/{id}` : 削除

### ✔ Exercise（種目）
- `POST /workouts/{id}/exercises` : 種目追加
- `GET /workouts/{id}/exercises` : 種目一覧
- `PATCH /exercises/{id}` : 名前変更
- `DELETE /exercises/{id}` : 削除

### ✔ Set（重量・回数）
- `POST /exercises/{id}/sets` : セット追加
- `GET /exercises/{id}/sets` : セット一覧
- `PATCH /sets/{id}` : 更新
- `DELETE /sets/{id}` : 削除

---

## 🚀 起動方法

```bash
uvicorn main:app --reload


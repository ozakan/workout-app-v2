# Workout App v2（筋トレ記録アプリ）

FastAPI + SQLAlchemy + React(TypeScript) を用いた、  
筋トレ内容（Workout / Exercise / Set）を記録・管理するための個人開発アプリです。

バックエンド設計の理解を深めることを目的に、  
REST API 設計・DB設計・責務分離を意識して実装しています。

---

## 技術スタック

### Backend
- FastAPI
- SQLAlchemy（ORM）
- SQLite（開発用）
- Pydantic

### Frontend（予定）
- React
- TypeScript
- Vite

---

## 機能概要（MVP）

- Workout（日付単位）の作成・取得・更新・削除
- Workout に紐づく Exercise の管理
- Exercise に紐づく Set（重量・回数）の管理
- 親子構造を持つネストJSONの取得
- 不正な操作に対する適切なステータスコード返却（404 / 409）

---

## API 設計

### Workout

| Method | Path | 内容 |
|------|------|------|
| POST | `/workouts` | Workout 作成 |
| GET | `/workouts` | Workout 一覧取得 |
| GET | `/workouts/{date}` | 日付指定で取得（Exercise / Set を含む） |
| PATCH | `/workouts/{workout_id}` | Workout 更新 |
| DELETE | `/workouts/{workout_id}` | Workout 削除 |

※ 同一日付の Workout 作成時は `409 Conflict` を返却

---

### Exercise（Workout 配下）

| Method | Path | 内容 |
|------|------|------|
| GET | `/workouts/{workout_id}/exercises` | Exercise 一覧 |
| POST | `/workouts/{workout_id}/exercises` | Exercise 作成 |
| PATCH | `/exercises/{exercise_id}` | Exercise 更新 |
| DELETE | `/exercises/{exercise_id}` | Exercise 削除 |

※ 親 Workout が存在しない場合は `404 Not Found`

---

### Set（Exercise 配下）

| Method | Path | 内容 |
|------|------|------|
| GET | `/exercises/{exercise_id}/sets` | Set 一覧 |
| POST | `/exercises/{exercise_id}/sets` | Set 作成 |
| PATCH | `/sets/{set_id}` | Set 更新 |
| DELETE | `/sets/{set_id}` | Set 削除 |

※ 親 Exercise が存在しない場合は `404 Not Found`

---

## 設計の工夫

- **親子関係が分かりやすいURL設計**
  - 一覧・作成は親リソース配下に配置
  - 更新・削除はリソースIDで直接操作

- **責務分離**
  - Router：HTTPリクエスト/レスポンス
  - CRUD：DB操作
  - Schema：入出力データ定義
  - Model：DB構造定義

- **DB整合性の担保**
  - 親リソース存在チェックによる 404 返却
  - unique 制約違反時の 409 Conflict

---

## 今後の予定

- 入力バリデーションの追加
- フロントエンド実装（React）
- PostgreSQL への移行

🏋️ Workout App v2

筋トレの記録を管理するための フルスタック Web アプリケーション です。
React（SPA）と FastAPI（REST API）を用いて、
Workout → Exercise → Set の階層構造でトレーニング内容を管理します。


🔧 技術スタック
フロントエンド
React
TypeScript
Vite
React Router（SPA）
fetch API

バックエンド
FastAPI
SQLAlchemy（ORM）
SQLite（※ 将来的に PostgreSQL へ移行予定）

🧩 アプリの構成
Workout（1日分）
 └─ Exercise（種目）
     └─ Set（重量・回数）


この構造をそのまま REST API とフロントエンドで扱っています。

🚀 現在できていること
フロントエンド
SPA 構成（ページ遷移時にリロードなし）
Workout 一覧 → 詳細画面への遷移
URL パラメータを用いた詳細表示
Workout → Exercise → Set の表示ロジック実装

バックエンド
SQLAlchemy の relationship を用いたモデル設計
ネストした JSON を返す REST API
GET /workouts/{date} による詳細取得
schemas / crud / routers に分離した設計

🔁 API 例
GET /workouts/{date}
{
  "id": 1,
  "date": "2025-12-05",
  "exercises": [
    {
      "id": 1,
      "name": "ベンチプレス",
      "sets": [
        { "id": 1, "weight": 80, "reps": 8 }
      ]
    }
  ]
}

🛣️ 今後の予定
POST / PATCH / DELETE API の実装（CRUD 完成）
フロントからの記録追加・編集
UI 改善（筋トレmemo風）
コンポーネント分割
Docker 化
PostgreSQL 対応

💡 開発方針
レイヤ分離
routers / crud / schemas / models
実務を意識した設計

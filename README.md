# Workout App v2（筋トレ記録アプリ）

FastAPI + SQLAlchemy を用いた、  
筋トレ内容（Workout / Exercise / Set）を記録・管理するための個人開発アプリです。

バックエンド設計の理解を深めることを目的に、  
REST API 設計・DB設計・認証・責務分離を意識して実装しています。

---

## 技術スタック

### Backend
- FastAPI
- SQLAlchemy（ORM）
- SQLite（開発用）
- Pydantic
- JWT認証
- python-dotenv（環境変数管理）

### Frontend
- 素のHTML + JavaScript
- FastAPIによる静的配信

---

## 機能概要

- ユーザー登録
- ログイン（JWT認証）
- ユーザーごとのデータ分離
- Workout（日付単位）の作成・取得・削除
- Workout に紐づく Exercise の管理
- Exercise に紐づく Set（重量・回数）の管理
- 親子構造を持つネストJSONの取得

---
## 設計のポイント
親子関係が分かりやすいREST設計
Router / CRUD / Schema / Model の責務分離
JWT認証によるユーザー分離
環境変数による秘密鍵管理

## 今後の予定
UI改善
グラフによるトレーニング可視化
PostgreSQLへの移行
Docker対応
デプロイ

# Workout App v2（筋トレ記録アプリ）

FastAPI + SQLAlchemy を用いた  
**Workout / Exercise / Set の親子構造を持つ筋トレ記録アプリ**の個人開発プロジェクトです。

バックエンドの REST API 設計と、  
**APIを実際に叩くフロントエンド実装（素のHTML/JavaScript）まで含めて**  
アプリケーション全体を通した設計・実装理解を目的としています。

---

## 技術スタック

### Backend
- FastAPI
- SQLAlchemy（ORM）
- SQLite（開発用）
- Pydantic

### Frontend（現状）
- HTML
- JavaScript（ES Modules）
- Fetch API

※ フレームワークを使わず、  
API設計と通信・状態更新の理解を優先しています。

---

## 機能概要（実装済み）

### Workout（1日単位）
- 作成 / 一覧取得 / 削除
- ID指定で詳細取得（Exercise / Set を含むネストJSON）

### Exercise（Workout配下）
- 作成 / 更新（名称変更） / 削除

### Set（Exercise配下）
- 作成（重量・回数）
- 更新
- 削除

👉 **Workout → Exercise → Set のフルCRUDを1画面で操作可能**

---

## 画面構成（現状）

- Workout一覧画面  
- Workout詳細画面  
  - Exercise一覧表示
  - 各Exerciseに紐づくSet一覧表示
  - Exercise / Set の追加・更新・削除を同一ページで実行

UIは簡易ですが、**機能検証を優先した構成**としています。

---

## 設計の工夫

- **RESTに沿ったURL設計**
  - 一覧・作成は親リソース配下
  - 更新・削除はID指定で直接操作

- **ネストJSONの活用**
  - Workout取得時に Exercise / Set をまとめて返却
  - フロント側の描画ロジックを簡潔に保持

- **責務分離**
  - Router：HTTP層
  - CRUD：DB操作
  - Schema：入出力定義
  - Model：DB構造

- **実装を伴う検証**
  - Swaggerだけでなく、実際の画面操作でAPIを検証

---

## 今後の予定

- 認証（JWT）の追加
- Workout一覧 → 詳細画面の導線整理
- UI改善（CSS）
- PostgreSQL への移行

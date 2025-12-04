from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite の DBファイル
SQLALCHEMY_DATABASE_URL = "sqlite:///./workout.db"

# DB接続エンジン
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLiteの場合必要
)

# セッション（DBと話すためのオブジェクト）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルが継承する基本クラス
Base = declarative_base()


# FastAPIで使う DB セッション依存性
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import os

from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from models import DatabaseModel
from models.functions.wrapper import DatabaseContext

load_dotenv()

# Load .env variables
DB_ENGINE = os.environ.get("DB_ENGINE")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")


def construct_sqlalchemy_url() -> URL:
    return URL.create(
        drivername=DB_ENGINE,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME,
        port=DB_PORT
    )

engine = create_async_engine(
    construct_sqlalchemy_url(),
    query_cache_size=1200,
    pool_size=100,
    max_overflow=200,
    future=True,
    echo=True,
)
database_session_pool = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

def get_db(model = DatabaseModel):
    return DatabaseContext(database_session_pool, query_model=model)
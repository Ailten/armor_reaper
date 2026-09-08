
from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    pass

# ------>


from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': getenv('DB_HOST'),
    'port': getenv('DB_PORT'),
    'database': getenv('DB_NAME'),
    'user': getenv('DB_LOGIN'),
    'password': getenv('DB_PASSWORD'),
}

# ------>


from sqlalchemy import URL, create_engine

from sqlalchemy.orm import sessionmaker

DB_URL = URL.create(
    drivername="mysql+pymysql",
    username=DB_CONFIG.get('user'),
    password=DB_CONFIG.get('password'),
    host=DB_CONFIG.get('host'),
    port=DB_CONFIG.get('port'),
    database=DB_CONFIG.get('database'),        
)
engine = create_engine(DB_URL, connect_args={"connect_timeout": 5})

# session builder.
sessionLocal = sessionmaker(bind=engine)

# inject session.
def get_db_session():
    with sessionLocal() as session:
        yield session
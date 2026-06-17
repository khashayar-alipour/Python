
# database.py

# موتور دیتابیس اینجا ساخته شده- ساخت این فایل مرحله اول هست

# برای ساخت دیتابیس میشه از mySQL یا sqlite یا postgre و ... استفاده کرد

# requirements:
    # pip install SQLalchemy
    
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base ,sessionmaker

# creating DB engine
engine = create_engine('sqlite:///quiz.db', echo=False)
SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    return SessionLocal()



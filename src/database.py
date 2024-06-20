from sqlalchemy.orm import sessionmaker
from config.settings import settings
from sqlalchemy import create_engine
from models import Base

engine = create_engine(url=settings.sqlite_dsn)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)


from sqlalchemy.orm import sessionmaker
from config.settings import settings
from sqlalchemy import create_engine, text
from .models import Base

engine = create_engine(url=settings.sqlite_dsn)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)

with open('db/insert_test_data.sql', 'r+') as file:
    sql_script = file.read()
    file.seek(0)
    file.truncate(0)


class InsertingTestData:
    """
    In case you want to add test data insert into insert_test_data.sql after one run of the func,
    insert_test_data will become empty.
    """
    @staticmethod
    def insert_data():
        with session() as conn:
            conn.execute(text(sql_script))
            conn.commit()



from src.database import session
from src.models import QueueRequests
from sqlalchemy import text


with open('../dbdir/insert_test_data.sql', 'r+') as file:
    sql_script = file.read()
    file.seek(0)
    file.truncate(0)


class TakeInfoFromQueueRequests:
    @staticmethod
    def fetch_requests():
        with session() as conn:
            conn.execute(text(sql_script))
            reqs = conn.query(QueueRequests)
            conn.commit()
        return reqs

from src.database import session
from src.models import QueueRequests


class TakeInfoFromQueueRequests:
    @staticmethod
    def fetch_requests():
        with session() as conn:
            return conn.query(QueueRequests).all()
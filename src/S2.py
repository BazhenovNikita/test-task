import time

from src.database import session
from models import QueueResponses, QueueRequests
from sqlalchemy import update, text


class WriteInfoInQueueResponses:
    @staticmethod
    def process_request(req):
        with session() as conn:
            if req.processed == 0:
                ustmt = update(QueueRequests).values(processed=True).filter_by(id=req.id)
                conn.execute(text(f"""INSERT INTO queue_responses (request_id, status_code, body) VALUES
                              ({req.id}, 200, '{req.url}');"""))
                time.sleep(1)
                conn.execute(ustmt)
                for r in conn.query(QueueResponses):
                    print(r.id, r.status_code, r.body)
                conn.commit()


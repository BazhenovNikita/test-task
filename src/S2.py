from src.database import session
from models import QueueResponses
from sqlalchemy import insert


class WriteInfoInQueueResponses:
    @staticmethod
    def process_request(reqs):
        notes = []
        for req in reqs:
            id, uri, method, params, headers, processed = req.id, req.url, req.method, req.params, req.headers, req.processed
            if processed != 1:
                notes.append({'request_id': id, 'status_code': 200, 'body': 'html file'})
        with session() as conn:
            stmt = insert(QueueResponses).values(notes)
            conn.execute(stmt)
            conn.commit()
        # if not processed:
        #
        #     url = f"{a_url}{uri}"
        #     params = json.loads(params)
        #     headers = json.loads(headers)
        #
        #     try:
        #         with request(method, url, params=params, headers=headers, timeout=timeout) as response:
        #             status_code = response.status_code
        #             body = response.text
        #     except RequestException as re:
        #         status_code = 500
        #         body = str(re)
        #
        #     with sqlite3.connect(db_path) as conn:
        #         cursor: Cursor = conn.cursor()
        #         cursor.execute("INSERT INTO queue_responses (request_id, status_code, body) VALUES (?, ?, ?)",
        #                        (id, status_code, body))
        #         cursor.execute('UPDATE queue_requests SET processed = 1 WHERE id = ?', (id,))
        #         conn.commit()

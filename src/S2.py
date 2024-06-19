import json
import sqlite3
from sqlite3 import Cursor

from requests import RequestException, request


class WriteInfoInQueueResponses:
    @staticmethod
    def process_request(req, a_url, db_path, timeout):
        id, uri, method, params, headers, processed = req
        if not processed:

            url = f"{a_url}{uri}"
            params = json.loads(params)
            headers = json.loads(headers)

            try:
                with request(method, url, params=params, headers=headers, timeout=timeout) as response:
                    status_code = response.status_code
                    body = response.text
            except RequestException as re:
                status_code = 500
                body = str(re)

            with sqlite3.connect(db_path) as conn:
                cursor: Cursor = conn.cursor()
                cursor.execute("INSERT INTO queue_responses (request_id, status_code, body) VALUES (?, ?, ?)",
                               (id, status_code, body))
                cursor.execute('UPDATE queue_requests SET processed = 1 WHERE id = ?', (id,))
                conn.commit()

from src.utils import CreateSqliteConnection, CreateMySqlConnection, CreatePostgreSqlConnection


class TakeInfoFromQueueRequests:
    @staticmethod
    def fetch_requests(db_path='db/queue_db.sqlite', **conn_var):
        if conn_var and conn_var['dbname']:
            conn = CreatePostgreSqlConnection.create_conn(**conn_var)
        elif conn_var:
            conn = CreateMySqlConnection.create_conn(**conn_var)
        else:
            conn = CreateSqliteConnection.create_conn(db_path)
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, uri, method, params, headers, processed FROM queue_requests")
            reqs = cursor.fetchall()
        return reqs

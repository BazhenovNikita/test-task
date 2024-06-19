from concurrent.futures import ThreadPoolExecutor

from src.S1 import TakeInfoFromQueueRequests
from src.S2 import WriteInfoInQueueResponses
from config.settings import settings

# передать в fetch_requests(**conn_var) если хотим работать с другими субд
conn_var = {
    'user': settings.user,
    'password': settings.password,
    'host': settings.host,
}


def main():
    reqs = TakeInfoFromQueueRequests.fetch_requests()
    for r in reqs:
        WriteInfoInQueueResponses.process_request(r, settings.url, settings.db_path, settings.timeout)


if __name__ == "__main__":
    main()

from src.S1 import TakeInfoFromQueueRequests
from src.S2 import WriteInfoInQueueResponses
from concurrent.futures import ThreadPoolExecutor
from config.settings import settings


def main():
    queries = TakeInfoFromQueueRequests.fetch_requests()
    with ThreadPoolExecutor(max_workers=settings.max_workers) as executor:
        executor.map(WriteInfoInQueueResponses.process_request, queries, timeout=settings.timeout)


if __name__ == "__main__":
    main()

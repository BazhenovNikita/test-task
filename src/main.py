from src.S1 import TakeInfoFromQueueRequests
from src.S2 import WriteInfoInQueueResponses
from src.database import InsertingTestData


def main():

    InsertingTestData.insert_data()
    reqs = TakeInfoFromQueueRequests.fetch_requests()
    r = WriteInfoInQueueResponses.process_request(reqs)


if __name__ == "__main__":
    main()

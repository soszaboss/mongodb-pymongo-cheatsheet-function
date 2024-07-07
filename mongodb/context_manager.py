from functools import wraps
import pymongo

class MongoContextManager:
    def __init__(self, url):
        self.url = url
        self.client = pymongo.MongoClient(self.url)

    def __enter__(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

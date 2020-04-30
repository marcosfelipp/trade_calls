from pymongo import MongoClient
import urllib.parse


class Database:
    def __init__(self, database, collection, user, password, host='localhost'):
        user, password = self.authenticate(user, password)
        self.mongo_client = MongoClient('mongodb://%s:%s@%s' % (user, password, host))
        self.database = database
        self.collection = collection

    def authenticate(self, user, password):
        username = urllib.parse.quote_plus(user)
        password = urllib.parse.quote_plus(password)
        return username, password

    def set_collection(self, collection):
        self.collection = collection

    def save_call(self, call, group=None):
        db = self.mongo_client[self.database][self.collection]
        db.insert_one(call.to_dict())

    def save_group(self, group):
        db = self.mongo_client[self.database][self.collection]
        db.insert_one()

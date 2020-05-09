from pymongo import MongoClient
import urllib.parse


def _database_authenticate(user, password):
    username = urllib.parse.quote_plus(user)
    password = urllib.parse.quote_plus(password)
    return username, password


class Database:
    def __init__(self, database, user, password, host='localhost'):
        user, password = _database_authenticate(user, password)
        self.mongo_client = MongoClient('mongodb://%s:%s@%s' % (user, password, host))
        self.database = database
        self.db = self.mongo_client[self.database]

    def drop_collection(self, collection):
        self.db[collection].drop()

    # ------------- CALS ------------- #

    def save_call(self, group_id, call):
        """
        Save call in group
        :param group_id: name of group
        :param call: call object
        :return: None
        """
        groups_collection = self.db["groups"]
        groups_collection.update({"_id": group_id}, {"$push": {"calls": call.to_dict()}})

    def get_calls(self, group_id):
        """
        Get list of calls in some group
        :param group_id: Name of group to search
        :return: Array with list of calls
        """
        groups_collection = self.db["groups"]
        return [i for i in groups_collection.find_one({"_id": group_id})['calls']]

    # ------------- GROUPS ------------- #

    def save_group(self, group):
        """
        Save group
        :param group: Group object
        :return: None
        """
        groups_collection = self.db["groups"]
        groups_collection.insert_one(group.to_dict())

    def get_groups(self, query=None):
        """
        Get list of groups or some group
        :param query: If not none, search for group name
        :return: Group or list of group
        """
        groups_collection = self.db["groups"]
        return [i for i in groups_collection.find(query)]

    # ------------- USERS ------------- #

    def save_user(self, user):
        """
        Save new user
        :param user: user object
        :return: None
        """
        user_collection = self.db["users"]
        user_collection.insert_one(user.to_dict())

    def get_user(self, user_name=None):
        """
        Get user by username
        :param user_name: user name
        :return: user if user_name is not none else list of all users
        """
        user_collection = self.db["users"]
        return user_collection.find(user_name)

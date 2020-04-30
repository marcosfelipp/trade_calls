from jsonschema import ValidationError
from bson import ObjectId


class Model(object):

    # __getattr__ = dict.get
    # __delattr__ = dict.__delitem__
    # __setattr__ = dict.__setitem__
    #
    # def save(self):
    #     if not self._id:
    #         self.collection.insert(self)
    #     else:
    #         self.collection.update(
    #             {"_id": ObjectId(self._id)}, self
    #         )
    #
    # def reload(self):
    #     if self._id:
    #         self.update(self.collection.find_one({"_id": ObjectId(self._id)}))
    #
    # def remove(self):
    #     if self._id:
    #         self.collection.remove({"_id": ObjectId(self._id)})
    #         self.clear()

    def to_dict(self):
        return self.__dict__


class CallModel(Model):
    def __init__(self, id, stock, type,
                 start, stop_loss, stop_gain, date, description=None, profit=None):
        self.id = id
        self.stock = stock
        self.type = type
        self.start = start
        self.stop_gain = stop_gain
        self.date = date
        self.description = description
        self.profit = profit

    @staticmethod
    def from_dict(data):
        return CallModel(**data)


class GroupModel():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_dict(data):
        return GroupModel(**data)


class UserModel():
    def __init__(self, username, password):
        self.username = username
        self.password = password
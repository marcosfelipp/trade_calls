import json


class Model(object):

    def to_dict(self):
        return self.__dict__


class CallModel(Model):
    def __init__(self, group_id, stock, type_call,
                 start, stop_loss, stop_gain, date, description=None, profit=None):
        self.group_id = group_id
        self.stock = stock
        self.type_call = type_call
        self.start = start
        self.stop_gain = stop_gain
        self.stop_loss = stop_loss
        self.date = date
        self.description = description
        self.profit = profit

    @staticmethod
    def from_dict(data):
        return CallModel(**data)


class GroupModel(Model):
    def __init__(self, name, user_administrator):
        self.name = name
        self.user_administrator = user_administrator

    @staticmethod
    def from_dict(data):
        return GroupModel(**data)

    def to_json(self):
        return json.dumps(self.to_dict())


class UserModel(Model):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def from_dict(data):
        return UserModel(**data)

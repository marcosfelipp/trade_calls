from marshmallow import Schema, fields, post_load, validate
from model import *


class CallSchema(Schema):
    user_administrator = fields.Str(required=True)
    stock = fields.Str(required=True)
    type_call = fields.Str(required=True)
    start = fields.Str(required=True)
    stop_gain = fields.Str()
    stop_loss = fields.Str()
    date = fields.Str(allow_none=False)
    description = fields.Str()
    profit = fields.Str(required=False)

    @post_load
    def make_model(self, data, **kwargs):
        return CallModel(**data)


class GroupSchema(Schema):
    name = fields.Str(required=True)
    calls = fields.List(fields.Dict, allow_none=True, default=[])

    @post_load
    def make_model(self, data, **kwargs):
        return GroupModel(**data)


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_model(self, data, **kwargs):
        return UserModel(**data)
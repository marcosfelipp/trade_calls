from marshmallow import Schema, fields, post_load
from tradecalldatabase.model import *


class CallSchema(Schema):
    group_id = fields.Str(required=True, data_key="groupId")
    stock = fields.Str(required=True)
    call_type = fields.Str(required=True, data_key="callType")
    start = fields.Str(required=True)
    stop_gain = fields.Str(data_key="stopGain")
    stop_loss = fields.Str(data_key="stopLoss")
    date = fields.Str(allow_none=False)
    description = fields.Str()
    profit = fields.Str(required=False)

    @post_load
    def make_model(self, data, **kwargs):
        return CallModel(**data)


class GroupSchema(Schema):
    _id = fields.UUID()
    user_owner = fields.Str(required=True, data_key="userOwner")
    name = fields.Str(required=True)
    description = fields.Str()
    img_url = fields.Str(data_key="imgUrl")

    @post_load
    def make_model(self, data, **kwargs):
        return GroupModel(**data)


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_model(self, data, **kwargs):
        return UserModel(**data)

from database import Database
from model import *
from schemas import *
from bson import ObjectId

if __name__ == "__main__":
    db = Database('notifications', 'teste', 'teste')
    db.drop_collection('groups')

    group = GroupSchema().load({"name": 'MorningCall'})
    db.save_group(group)

    group = GroupSchema().load({"name": 'Empiricus'})
    db.save_group(group)

    id = db.get_groups({"name": "MorningCall"})[0]['_id']
    call = CallSchema().load({"user_administrator": ObjectId().__str__(),
                              "stock": 'OIBR3',
                              "type_call": 'compra',
                              "start": '0,61',
                              "stop_gain": '0,60',
                              "stop_loss": '0,65',
                              "date": 'now'})
    db.save_call(id, call)

    call = CallSchema().load({"user_administrator": ObjectId().__str__(),
                              "stock": 'PETR4',
                              "type_call": 'venda',
                              "start": '0,61',
                              "stop_gain": '0,60',
                              "stop_loss": '0,65',
                              "date": 'now'})
    db.save_call(id, call)

    for i in db.get_calls(id):
        print(i)
from database import Database
from schemas import *
from flask import Flask, jsonify

if __name__ == "__main__":
    db = Database('notifications', 'teste', 'teste')
    db.drop_collection('groups')
    db.drop_collection('users')
    db.drop_collection('calls')

    user = UserSchema().load({"username": "admin",
                              "password": "password"})

    db.save_user(user)
    user_id = db.get_user({"username": "admin"})[0]["_id"]

    group = GroupSchema().load({"name": 'MorningCall',
                                "user_administrator": str(user_id)})
    db.save_group(group)

    group = GroupSchema().load({"name": 'Empiricus',
                                "user_administrator": str(user_id)})
    db.save_group(group)

    group_id = db.get_groups({"name": "MorningCall"})[0]['_id']

    call = CallSchema().load({"group_id": str(group_id),
                              "stock": 'OIBR3',
                              "type_call": 'compra',
                              "start": '0,61',
                              "stop_gain": '0,60',
                              "stop_loss": '0,65',
                              "date": 'now'})
    db.save_call(call)

    call = CallSchema().load({"group_id": str(group_id),
                              "stock": 'PETR4',
                              "type_call": 'venda',
                              "start": '0,61',
                              "stop_gain": '0,60',
                              "stop_loss": '0,65',
                              "date": 'now'})
    db.save_call(call)

    # Get calls of a group:
    for i in db.get_calls({"group_id": str(group_id)}):
        print(i)

    # Get groups of user:

    groups = db.get_groups({"user_administrator": str(user_id)})
    print(groups)

    g = GroupSchema(many=True).dump(groups)

    print(jsonify(g))

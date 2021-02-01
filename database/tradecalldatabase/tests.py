from database import Database
from schemas import *
from flask import Flask, jsonify

if __name__ == "__main__":
    db = Database('notifications', 'test', 'test')
    db.drop_collection('groups')
    db.drop_collection('users')
    db.drop_collection('calls')

    user = UserSchema().load({"username": "admin",
                              "password": "password"})

    db.save_user(user)
    user_id = db.get_user({"username": "admin"})[0]["_id"]

    group = GroupSchema().load({"name": 'MorningCall',
                                "userOwner": str(user_id),
                                "description": "calls diários para compras na manhã",
                                "imgUrl": "https://5be8c0f6d904e0044d904cc1.static-01.com/l/images/e8e10145e2e40270acb0fce8da3c5eb8529e3652.jpg"})
    db.save_group(group)

    group = GroupSchema().load({"name": 'Empiricus',
                                "userOwner": str(user_id),
                                "description": "Receba calls toda semana",
                                "imgUrl": "https://uploads-ssl.webflow.com/5c474935f83b6b7ee2a3fe1d/5d5ea6fae396d1fc71693e8f_o-que-e-como-fazer-trade-de-criptomoedas.jpg"})
    db.save_group(group)

    group_id = db.get_groups({"name": "MorningCall"})[0]['_id']

    call = CallSchema().load({"groupId": str(group_id),
                              "stock": 'OIBR3',
                              "callType": 'compra',
                              "start": '0,61',
                              "stopGain": '0,60',
                              "stopLoss": '0,65',
                              "date": 'now'})
    db.save_call(call)

    call = CallSchema().load({"groupId": str(group_id),
                              "stock": 'PETR4',
                              "callType": 'venda',
                              "start": '0,61',
                              "stopGain": '0,60',
                              "stopLoss": '0,65',
                              "date": 'now'})
    db.save_call(call)

    # Get calls of a group:
    for i in db.get_calls({"group_id": str(group_id)}):
        print(i)

    # Get groups of user:
    # groups = db.get_groups({'user_owner': str(user_id)})
    # groups = GroupSchema(many=True).dump(groups)
    # print(groups)

    print("User: {}".format(user_id))
    print("Grupo: {}".format(group_id))

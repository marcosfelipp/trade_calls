from database import Database
from model import *

if __name__ == "__main__":
    db = Database('notifications', 'teste', 'teste')
    db.drop_collection('groups')

    group = GroupModel('MorningCall')
    db.save_group(group)

    call = CallModel('0', 'OIBR3', 'compra', '0,61', '0,60', '0,65', 'now')
    db.save_call('MorningCall', call)

    call = CallModel('0', 'OIBR3', 'venda', '0,61', '0,60', '0,65', 'now')
    db.save_call('MorningCall', call)

    call = CallModel('0', 'PETR4', 'venda', '14', '13', '12', 'now')
    db.save_call('MorningCall', call)

    for i in db.get_calls('MorningCall'):
        print(i)
from database import Database
from model import *

if __name__ == "__main__":
    call = CallModel('0', 'OIBR3', 'compra', '0,61', '0,60', '0,65', 'now')

    db = Database('notifications', 'calls', 'teste', 'teste')
    db.save_call(call)
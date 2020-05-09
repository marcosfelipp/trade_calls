import logging
from flask import Flask, jsonify, request
import pika
from tradecalldatabase.database import Database
from tradecalldatabase.schemas import GroupSchema, CallSchema

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# RabbitMQ configurations:
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='trade_notifications')

# logging
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)

# Database
db = Database('notifications', 'teste', 'teste')

#########################
# ROUTERS
#########################


@app.route('/api/v1/new_user', methods=['POST'])
def post_register_user():
    pass


@app.route('/api/v1/call', methods=['POST'])
def post_call():
    message = str(request.get_json())

    logger.debug("Data received {}: ".format(message))
    channel.basic_publish(exchange='',
                          routing_key='trade_notifications',
                          body=message)

    return jsonify({'data': "OK"})


@app.route('/api/v1/calls/<string:group_id>', methods=['GET'])
def get_calls(group_id):
    """
    Get calls of a group
    :param group_id: Group identification
    :return: List of calls
    """
    calls = db.get_calls({"group_id": group_id})
    calls = CallSchema(many=True).dump(calls)
    return jsonify(calls)


def post_call_performance():
    pass


@app.route('/api/v1/groups/<string:user_id>', methods=['GET'])
def get_groups(user_id):
    """
    Get all group of an user
    :param user_id: username
    :return: List of Groups
    """
    groups = db.get_groups({'user_owner': str(user_id)})
    groups = GroupSchema(many=True).dump(groups)
    return jsonify(groups)


@app.route('/api/v1/group', methods=['POST'])
def post_group():
    pass


@app.route('/api/v1/group/user', methods=['POST'])
def add_user_group():
    pass

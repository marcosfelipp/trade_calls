import logging
from flask import Flask, jsonify, request, send_file
import pika

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

#########################
# ROUTERS
#########################


@app.route('/api/v1/call', methods=['POST'])
def post_call():
    message = str(request.get_json())

    logger.debug("Data received {}: ".format(message))
    channel.basic_publish(exchange='',
                          routing_key='trade_notifications',
                          body=message)

    return jsonify({'data': "OK"})


@app.route('/api/v1/call', methods=['GET'])
def get_calls():
    calls = [{
        "ativo": 'PETR4',
        "tipo": 'venda',
        "entrada": '50',
        "stopLoss": '40',
        "stopGain": '60',
        "description": 'Vende galera',
    }, {
        "ativo": 'OIBR3',
        "tipo": 'compra',
        "entrada": '50',
        "stopLoss": '40',
        "stopGain": '60',
        "description": 'Compra galera',
    }]

    return jsonify(calls)


@app.route('/api/v1/new_user', methods=['POST'])
def post_register_user():
    pass


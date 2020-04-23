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

#########################
# ROUTERS
#########################


@app.route('/api/v1/new_call', methods=['POST'])
def post_call():
    message = str(request.form['message'])
    channel.basic_publish(exchange='',
                          routing_key='trade_notifications',
                          body=message)

    return jsonify({'data': "OK"})


@app.route('/api/v1/new_user', methods=['POST'])
def post_register_user():
    pass
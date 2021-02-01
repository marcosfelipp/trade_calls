import pika
import json
import logging

from settings import TELEGRAM_TOKEN
from telegram import Bot
from image_generator import *

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('telegram')
logger.setLevel(logging.DEBUG)

def send_message(chat_id, message):
    message = json.loads(message.decode())
    stock = message["stock"]
    type = "Compra" if message["type"] == 1 else "Venda"
    start = message["start"]
    stop_loss = message["stopLoss"]
    stop_gain = message["stopGain"]
    description = message["description"]

    msg_to_send = "Nova call\n:Ativo: {}\nTipo: {}\nEntrada: {}\nStop Gain: {}\nStop Loss: {}".format(
        stock, type, start, stop_gain, stop_loss
    )

    generate_image(stock, type, start, stop_loss, stop_gain)
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.sendMessage(chat_id=chat_id, text=msg_to_send)
    bot.sendPhoto(chat_id=chat_id, photo=open('out.png', 'rb'))


def subscribe_topic(channel, topic):
    channel.queue_declare(queue=topic)
    channel.basic_consume(queue=topic,
                          auto_ack=True,
                          on_message_callback=callback)


def callback(ch, method, properties, body):
    send_message('-1001380218326', body)


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-service'))
    ch = connection.channel()

    subscribe_topic(ch, "trade_notifications")
    print(' [*] Waiting for messages. To exit press CTRL+C')
    ch.start_consuming()



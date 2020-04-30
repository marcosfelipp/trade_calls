import pika

from settings import TELEGRAM_TOKEN
from telegram import Bot
from image_generator import *


def send_message(chat_id, message):
    generate_image('OIBR3', 'venda', '0,60', '0,55', '0,50')
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.sendMessage(chat_id=chat_id, text=message)
    bot.sendPhoto(chat_id=chat_id, photo=open('out.png', 'rb'))


def subscribe_topic(channel, topic):
    channel.queue_declare(queue=topic)
    channel.basic_consume(queue=topic,
                          auto_ack=True,
                          on_message_callback=callback)


def callback(ch, method, properties, body):
    send_message('-1001380218326', str(body))


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0'))
    ch = connection.channel()

    subscribe_topic(ch, "trade_notifications")
    print(' [*] Waiting for messages. To exit press CTRL+C')
    ch.start_consuming()



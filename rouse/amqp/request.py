import pika
from django.conf import  settings

class Request(object):
	def __init__(self):
		self.username = settings.RABBITMQ_CONFIG.get("USERNAME")
		self.password = settings.RABBITMQ_CONFIG.get("PASSWORD")
		self.host = settings.RABBITMQ_CONFIG.get("HOST")
		self.port = settings.RABBITMQ_CONFIG.get("PORT")
		self.vhost = settings.RABBITMQ_CONFIG.get("VHOST")

	def connect(self):
		user_pwd = pika.PlainCredentials(self.username, self.password)
		s_conn = pika.BlockingConnection(pika.ConnectionParameters(
			host= self.host,
			port=self.port,
			credentials=user_pwd,
			virtual_host = self.vhost
		))  # 创建连接
		self.channel = s_conn.channel()

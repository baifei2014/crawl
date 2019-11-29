from rouse.amqp.request import Request

class Consumer(Request):
    def consume(self, queuename, closure):
        self.connect()
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=queuename,
            auto_ack=True,
            on_message_callback=closure
        )
        self.channel.start_consuming()
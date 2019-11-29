from django.core.management.base import BaseCommand
from rouse.amqp.consumer import Consumer
import json
from rouse.models import Schedule
from rouse.crawl.chromecrawl import ChromeCrawl
from django.conf import  settings

def callback(ch, method, properties, body):
    data = json.loads(body)

    schedule = Schedule.objects.get(id=data['id'])
    schedule.setScheduleProcessing()

    base_dir = settings.CRAWL_IMAGE_BASE_DIR
    chromeCrawl = ChromeCrawl()
    chromeCrawl.crawl(schedule.url, schedule.id, base_dir)

    schedule.setScheduleCompleted()

class Command(BaseCommand):
    def handle(self, *args, **options):
        consumer = Consumer()
        consumer.consume("imageCrawl", callback)
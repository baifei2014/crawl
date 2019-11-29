from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlretrieve
import ssl
import os
ssl._create_default_https_context = ssl._create_unverified_context


# class HelloWorldViewSet(GenericViewSet):

#     @action(detail=False)
#     def world(self, request, *args, **kwargs):
#         return Response({"code": 0, "msg": "hello world!"})
#         log = logs.logger()

class ImageCrawlViewSet(GenericViewSet):

	@action(detail=False)
	def crawl(self, request, *args, **kwargs):
		imgBaseDir = os.getenv('CRAWL_IMAGE_BASE_DIR', '/data/source/image')

		return Response({"code": 0, "msg": "你好，这里是007", "dir": imgBaseDir})
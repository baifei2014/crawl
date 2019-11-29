from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from urllib.request import urlretrieve
import ssl
import os
import datetime
import hashlib
from rouse.models import Image
ssl._create_default_https_context = ssl._create_unverified_context

class ChromeCrawl(object):
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--headless')
		self.driver = webdriver.Chrome(chrome_options=chrome_options)

	def crawl(self, url, releation_id, base_dir):
		self.driver.get(url)
		time.sleep(5)
		self.driver.switch_to.frame('content-body');

		file_dir = self.getDir(base_dir)
		if not os.path.exists(file_dir):
			os.makedirs(file_dir)

		eles = self.driver.find_elements_by_css_selector("#noteIFrameContent div")
		for i in eles:
			if not i.get_attribute("yne-bulb-block") == 'image':
				continue
			filename = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()

			real_file = "%s%s.jpg" % (str(file_dir), str(filename))
			urlretrieve(i.find_element_by_tag_name("img").get_attribute('data-original'), real_file)

			if os.path.exists(real_file):
				image = Image(schedule_id=releation_id, path=real_file, name=filename)
				image.save()
		self.driver.close()

	def getDir(self, base_dir):
		if not str(base_dir).endswith('/'):
			base_dir = '%s/' % base_dir

		return '%s%s/%s/%s/' %(base_dir, time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'))

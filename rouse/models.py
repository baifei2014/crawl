from django.db import models

# Create your models here.
class Schedule(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	url = models.CharField(max_length=1024)
	status = models.IntegerField(default=0)
	is_delete = models.IntegerField(default=0)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def setScheduleProcessing(self):
		self.status = 1
		self.save()

	def setScheduleCompleted(self):
		self.status = 2
		self.save()

class Image(models.Model):
	id = models.AutoField(primary_key=True)
	schedule_id = models.IntegerField()
	name = models.CharField(max_length=255)
	path = models.CharField(max_length=1024)
	is_delete = models.IntegerField(default=0)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
		

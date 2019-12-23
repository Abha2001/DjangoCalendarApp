from django.db import models



# Create your models here.
class Events(models.Model):
	EventName=models.CharField(max_length=200)
	startTime=models.DateTimeField()
	endTime=models.DateTimeField()

	def __str__(self):
		return self.EventName
	class Meta:
		verbose_name_plural='Events'


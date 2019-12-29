from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Event(models.Model):
	day=models.DateField(default=date.today())
	start_time=models.TimeField()
	end_time=models.TimeField()
	notes=models.CharField(max_length=200)

	class Meta:
		verbose_name_plural='Events'

	def get_absolute_url(self):
		url=reverse('admin:cal_%s_change'%(self._meta.model_name),args=[self.id])
		return '<a href="%s">%s</a>'%(url,str(self.notes))



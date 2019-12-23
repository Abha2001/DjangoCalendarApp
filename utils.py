from datetime import datetime
from .models import Events
from calendar import HTMLCalendar

class Calendar(HTMLCalendar):
	def __init__(self,year=None,month=None):
		super(Calendar,self).__init__()
		self.year=year
		self.month=month

	def formatday(self,day,events):
		eventsInOneDay=events.filter(startTime__day=day)
		d=''
		for i in eventsInOneDay:
			d+=f'<li>{event.EventName}<li>'

		if day!=0:
			return f'<td><span class='date'>{day}</span><ul>{d}</ul></td>'

		return '<td></td>'

	
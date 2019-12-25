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
			return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"

		return '<td></td>'

	def formatweek(self,theweek,events):
		week=''
		for d in theweek:
			week+=self.formatday(d,events)
		return f'<tr>{week}</tr>'

	def formatmonth(self,withyear='True'):
		events=Events.objects.filter(startTime__year=self.year,startTime__month=self.month)

		cal=f"<table border='0' cell padding='0' cellspacing='0' class='calendar'>\n"
		cal+=f'{self.formatmonthname(self.year,self.month,withyear=withyear)}\n'
		cal+=f'<self.formatweekheader()>\n'
		for week in self.monthdays2calendar(self.year,self.month):
			cal+=f'{self.formatweek(week,events)}\n'
		return cal





from datetime import datetime
from .models import Event
from calendar import HTMLCalendar

class EventCalendar(HTMLCalendar):
	def __init__(self,events=None):
		super(EventCalendar,self).__init__()
		self.events=events

	def formatday(self,day,weekday,events):
		eventsInOneDay=events.filter(day__day=day)
		events_html="<ul>"
		for event in eventsInOneDay:
			events_html+=event.get_absolute_url()+"<br>"
		events_html+="</ul>"
		

		if day==0:
			return '<td class="noday">&nbsp;</td>'
		return '<td class="date">%d%s</td>'%(day,events_html)

	def formatweek(self,theweek,events):
		s=''.join(self.formatday(d,wd,events) for (d,wd) in theweek)
		return '<tr>%s</tr>'%s

	def formatmonth(self,theyear,themonth,withyear=True):
		events=Event.objects.filter(day__month=themonth)

		v=[]
		a=v.append
		a('<table border="0" cell padding="0" cellspacing="0" class="table table-striped table-hover table-bordered">')
		a('\n')
		a(self.formatmonthname(theyear,themonth,withyear=withyear))
		a('\n')
		a(self.formatweekheader())
		a('\n')
		for week in self.monthdays2calendar(theyear,themonth):
			a(self.formatweek(week,events))
			a('\n')
		a('</table>')
		a('\n')
		return ''.join(v)

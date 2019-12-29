from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import EventCalendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self,**kwargs):
        context =super().get_context_data(**kwargs)
        
        day= self.request.GET.get('day_gte', None)
        
        if not day:
        	d=datetime.date.today()
        else:
        	try:
        		split_day=day.split('-')
        		d=datetime.date(year=int(split_day[0]),month=int(split_day[1]),day=1)
        	except:
        		d=datetime.date.today()


        cal = EventCalendar()
        html_cal = cal.formatmonth(d.year,d.month,withyear=True)
        html_cal=html_cal.replace('<td','<td width="200" height="80"')
        context['calendar']= mark_safe(html_cal)
        return context



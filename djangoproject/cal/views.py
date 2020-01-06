from django.shortcuts import render,get_object_or_404
import datetime
import calendar
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .utils import EventCalendar
from django.urls import reverse
from .forms import EventForm

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
        html_cal=html_cal.replace('<td','<td width="500" height="80"')
        context['calendar']= mark_safe(html_cal)
        context['prev_month']=str(prev_month(d))
        context['next_month']=str(next_month(d))
        return context

def prev_month(d):
    first=d.replace(day=1)
    prev_month=first-datetime.timedelta(days=1)
    month=str(prev_month.year)+'-'+str(prev_month.month)
    return month

def next_month(d):
    days_in_month=calendar.monthrange(d.year,d.month)[1]
    last=d.replace(day=days_in_month)
    next_month=last+datetime.timedelta(days=1)
    month=str(next_month.year)+'-'+str(next_month.month)
    return month

def event(request,event_id=None):
    instance=Event()
    if event_id:
        instance=get_object_or_404(Event,pk=event_id)
    else:
        instance=Event()

    form=EventForm(request.POST or None,instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request,'cal/event.html',{'form':form})



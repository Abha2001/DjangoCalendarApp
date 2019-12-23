from django.shortcuts import render
from .models import Events
from .util import Calendar
# Create your views here.

class CalView(generic.ListView):
	model=Events
	template_name='cal/calender.html'

	def date(self):
		
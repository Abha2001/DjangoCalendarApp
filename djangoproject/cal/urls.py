from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views

app_name='cal'

urlpatterns=[
	path('Calendar/',views.CalendarView.as_view(),name='calendar'),
	path('event/new/',views.event,name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/',views.event,name='event_edit'),
]

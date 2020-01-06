from django.forms import ModelForm,DateInput
from cal.models import Event

class EventForm(ModelForm):
	class Meta:
		model=Event
		widgets={
		'day':DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%d'),
		'start_time':DateInput(attrs={'type':'datetime-local'},format='%H:%M:%S'),
		'end_time':DateInput(attrs={'type':'datetime-local'},format='%H:%M:%S')
		}

		fields='__all__'

	def __init__(self,*args,**kwargs):
		super(EventForm,self).__init__(*args,**kwargs)

		self.fields['day'].input_formats=('%Y-%m-%d',)
		self.fields['start_time'].input_formats=('%H:%M:%S',)
		self.fields['end_time'].input_formats=('%H:%M:%S',)

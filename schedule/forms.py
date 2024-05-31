from django import forms
from schedule.models import Event

class EventForm(forms.ModelForm):
        
        class Meta:
                model = Event
                fields = ['title', 'description', 'date_event', 'participant', 'event_type']
                widgets = {
			'date_event' : forms.DateTimeInput(attrs={'type' : 'datetime-local'})
		}
from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

class Event(models.Model):
        
        EVENT_TYPE = {
		'BIRTHDAY' : 'Birthday',
		'MEETING' : 'Meeting',
		'WORK' : 'Work',
		'HOLIDAY' : 'Holiday',
		'COURSE' : 'Course',
		'PARTY' : 'Party',
		'CULTURAL_ACTIVITY' : 'Cultural activity',
		'SPORT_ACTIVITY' : 'Sport activity',
		'MEDICAL' : 'Medical',
		'SPECIAL' : 'Special',
		'OTHER' : 'Other',
	}
        
        title = models.CharField(max_length=128)
        description = models.CharField(max_length=2000, null=True, blank=True)
        date_created = models.DateTimeField(auto_now_add=True)
        date_event = models.DateTimeField()
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_authored')
        participant = models.ManyToManyField(User, through="EventParticipation", related_name='participants')
        event_type = models.CharField(max_length=17, choices=EVENT_TYPE)
        
        def __str__(self):
                return self.title

class EventParticipation(models.Model):
        
        event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participations')
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participated_events')
        participation = models.BooleanField(default=False)
        
        class Meta:
                unique_together = ('event', 'user')
                
        @transaction.atomic
        def participate(self):
                self.participation = not self.participation
                self.save()

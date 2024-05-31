from django.contrib import admin
from schedule.models import Event, EventParticipation

admin.site.register(Event)
admin.site.register(EventParticipation)

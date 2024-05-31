from django.shortcuts import render, redirect
from schedule.models import Event, EventParticipation
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q, QuerySet
from schedule.forms import EventForm

User = get_user_model()

@login_required
def schedule(request):
        
        now = datetime.now()
        
        events_authored = request.user.events_authored.filter(Q(date_event__gte=now))
        events_participant = request.user.participants.filter(Q(date_event__gte=now))
        events = (events_authored | events_participant).distinct().order_by('date_event')
        return render(request, 'schedule/schedule.html', {'events' : events})

@login_required
def event_create(request):
        
        event_form = EventForm()
        
        if request.method == 'POST':
                print(request.POST)
                event_form = EventForm(request.POST)
                if event_form.is_valid():
                        event = event_form.save(commit=False)
                        event.author = request.user
                        event.date_event = datetime.strptime(request.POST['date_event'], '%Y-%m-%dT%H:%M')
                        event.save()
                        participants = request.POST.getlist('participant')
                        for user_id in participants:
                                event.participant.add(user_id)
                        return redirect('schedule')
        return render(request, 'schedule/event_create.html', {'event_form' : event_form})

@login_required
def event_detail(request, id):
        
        event = Event.objects.get(id=id)
        event_participation = EventParticipation.objects.filter(Q(event=event) & Q(user_id=request.user.id)).first()
        users_invited = User.objects.filter(participants=event)
        participates = EventParticipation.objects.filter(Q(event=event))
        
        
        if event_participation:
                return render(request, 'schedule/event_detail.html', {'event' : event, 'users_invited' : users_invited, 'event_participation' : event_participation, 'participates' : participates})
        elif request.user.id == event.author.id:
                return render(request, 'schedule/event_detail.html', {'event' : event, 'users_invited' : users_invited, 'participates' : participates})
        else:
                return redirect('schedule')

@login_required     
def event_participate(request, id):
        
        event = Event.objects.get(id=id)
        event_participation = EventParticipation.objects.filter(Q(event=event) & Q(user_id=request.user.id)).first()
        
        if event_participation:
                if event_participation.participation == True:
                        event_participation.participation = False
                else:
                        event_participation.participation = True
                event_participation.save()
        return redirect('event-detail', event.id)

@login_required
def event_delete(request, id):
        
        event = Event.objects.get(id=id)
        
        if event.author == request.user:
                if request.method == 'POST':
                        event.delete()
        return redirect('schedule')

@login_required
def event_edit(request, id):
        
        event = Event.objects.get(id=id)
        event_form = EventForm(instance=event)
        
        if request.method == 'POST':
                event_form = EventForm(request.POST, instance=event)
                if event_form.is_valid():
                        event_form.save()
                        participants = request.POST.getlist('participant')
                        event.participant.set(participants)
                        return redirect('event-detail', event.id)
        return render(request, 'schedule/event_edit.html', {'event_form' : event_form})
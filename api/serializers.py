from rest_framework import serializers
from task.models import Task
from schedule.models import Event, EventParticipation
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'birthday']

class UserDetailSerializer(serializers.ModelSerializer):
        
        tasks_authored = serializers.SerializerMethodField()
        tasks_received = serializers.SerializerMethodField()
        events_authored = serializers.SerializerMethodField()
        participated_events = serializers.SerializerMethodField()
        
        class Meta:
                model = User
                fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'birthday', 'tasks_authored', 'tasks_received', 'events_authored', 'participated_events']
                
        def get_tasks_authored(self, instance):
                queryset = instance.tasks_authored
                serializers = TaskListSerializer(queryset, many=True)
                return serializers.data
        
        def get_tasks_received(self, instance):
                queryset = instance.tasks_received
                serializers = TaskListSerializer(queryset, many=True)
                return serializers.data
        
        def get_events_authored(self, instance):
                queryset = instance.events_authored
                serializers = EventListSerializer(queryset, many=True)
                return serializers.data
        
        def get_participated_events(self, instance):
                queryset = instance.participated_events
                serializers = EventParticipationListSerializer(queryset, many=True)
                return serializers.data

class TaskListSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = Task
                fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'finish']

class TaskDetailSerializer(serializers.ModelSerializer):
        
        author = UserListSerializer()
        target = UserListSerializer()
        
        class Meta:
                model = Task
                fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'finish', 'author', 'target']
                
        def get_author(self, instance):
                queryset = instance.author
                serializer = UserListSerializer(queryset)
                return serializer.data
        
        def get_target(self, instance):
                queryset = instance.target
                serializer = UserListSerializer(queryset)
                return serializer.data

class EventDetailSerializer(serializers.ModelSerializer):
        
        author = serializers.SerializerMethodField()
        participant = serializers.SerializerMethodField()
        event_participations = serializers.SerializerMethodField()
        
        class Meta:
                model = Event
                fields = ['id', 'title', 'description', 'date_created', 'date_event', 'event_type', 'author', 'participant', 'event_participations']
        
        def get_author(self, instance):
                queryset = instance.author
                serializers = UserListSerializer(queryset)
                return serializers.data
        
        def get_participant(self, instance):
                queryset = instance.participant
                serializers = UserListSerializer(queryset, many=True)
                return serializers.data
        
        def get_event_participations(self, instance):
                queryset = instance.event_participations
                serializers = EventParticipationListSerializer(queryset, many=True)
                return serializers.data

class EventListSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = Event
                fields = ['id', 'title', 'description', 'date_created', 'date_event', 'event_type']

class EventParticipationListSerializer(serializers.ModelSerializer):
        
        class Meta:
                model = EventParticipation
                fields = ['id', 'participation']

class EventParticipationDetailSerializer(serializers.ModelSerializer):
        
        event = serializers.SerializerMethodField()
        user = serializers.SerializerMethodField()
        
        class Meta:
                model = EventParticipation
                fields = '__all__'
                
        def get_event(self, instance):
                queryset = instance.event
                serializers = EventListSerializer(queryset)
                return serializers.data
        
        def get_user(self, instance):
                queryset = instance.user
                serializers = UserListSerializer(queryset)
                return serializers.data
        
        
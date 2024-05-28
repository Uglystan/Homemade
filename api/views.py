from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from task.models import Task
from schedule.models import Event,EventParticipation
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from django.db import transaction
from api.serializers import TaskDetailSerializer, UserListSerializer, TaskListSerializer, UserDetailSerializer, EventDetailSerializer, EventListSerializer, EventParticipationDetailSerializer, EventParticipationListSerializer
from api.permisisons import IsAdmin

User = get_user_model()

class AdminTaskViewset(ModelViewSet):
        list_serializer_class = TaskListSerializer
        detail_serializer_class = TaskDetailSerializer
        permission_classes = [IsAdmin, IsAuthenticated]
        
        def get_queryset(self):
                return Task.objects.all()
        
        def get_serializer_class(self):
                if self.action == 'retrieve':
                        self.detail_serializer_class
                return self.list_serializer_class
                

class TaskViewset(ReadOnlyModelViewSet):
        list_serializer_class = TaskListSerializer
        detail_serializer_class = TaskDetailSerializer
        
        def get_queryset(self):
                return Task.objects.all()
        
        def get_serializer_class(self):
                if self.action == 'retrieve':
                        return self.detail_serializer_class
                return self.list_serializer_class
        
        @action(methods=['post'], detail=True)
        @transaction.atomic
        def done(self, request, pk):
                task = self.get_object()
                task.done()
                return Response()
        

class UserViewset(ReadOnlyModelViewSet):
        list_serializer_class = UserListSerializer
        detail_serializer_class = UserDetailSerializer
        
        def get_queryset(self):
                return User.objects.all()
        
        def get_serializer_class(self):
                if self.action == 'retrieve':
                        return self.detail_serializer_class
                return self.list_serializer_class
        

class EventViewset(ReadOnlyModelViewSet):
        
        list_serializer_class = EventListSerializer
        detail_serializer_class = EventDetailSerializer
        
        def get_queryset(self):
                return Event.objects.all()
        
        def get_serializer_class(self):
                if self.action == 'retrieve':
                        return self.detail_serializer_class
                return self.list_serializer_class
        
        
class EventParticipationViewset(ReadOnlyModelViewSet):
        
        list_serializer_class = EventParticipationListSerializer
        detail_serializer_class = EventParticipationDetailSerializer
        
        def get_queryset(self):
                return EventParticipation.objects.all()
        
        def get_serializer_class(self):
                if self.action == 'retrieve':
                        return self.detail_serializer_class
                return self.list_serializer_class
        
        @action(methods=['post'], detail=True)
        @transaction.atomic
        def participate(self, request, pk):
                event_participation = self.get_object()
                event_participation.participate()
                return Response()
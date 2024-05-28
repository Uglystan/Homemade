from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def home(request):
        tasks = request.user.tasks_received.filter(finish=False)
        return render(request, 'home/home.html', {'tasks' : tasks})
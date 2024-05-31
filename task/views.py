from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from task.forms import TaskForm
from task.models import Task
from django.views import View

@method_decorator(login_required, name='dispatch')
class TaskView(View):
        def get(self, request):
                tasks_authored = request.user.tasks_authored.all()
                tasks_received = request.user.tasks_received.all()
                task_form = TaskForm()
                
                context = {
                        'tasks_authored' : tasks_authored,
			'tasks_received' : tasks_received,
			'task_form' : task_form,
		}
                
                return render(request, 'task/task.html', context=context)

@login_required
def task_create(request):
        task_form = TaskForm()
        
        if request.method == 'POST':
                task_form = TaskForm(request.POST)
                if task_form.is_valid():
                        task = task_form.save(commit=False)
                        task.author = request.user
                        task.save()
                        return redirect('task')
        return render(request, 'task/task_create.html', {'task_form' : task_form})

@login_required
def task_detail(request, id):
        task = Task.objects.get(id=id)
        if request.user == task.author or request.user == task.target:
                return render(request, 'task/task_detail.html', {'task' : task})
        else:
                return redirect('task')
         

@login_required
def task_edit(request, id):
        task = Task.objects.get(id=id)
        task_form = TaskForm(instance=task)
        
        if request.user == task.author:
                if request.method == 'POST':
                        task_form = TaskForm(request.POST, instance=task)
                        if task_form.is_valid():
                                task = task_form.save()
                                return redirect('task-detail', task.id)
                return render(request, 'task/task_edit.html', {'task_form' : task_form})
        else:
                return redirect('task-detail', task.id)

@login_required
def task_done(request, id):
        task = Task.objects.get(id=id)
        
        if task.author == request.user or task.target == request.user:
                task.finish = True
                task.save()
        return redirect('task-detail', task.id)

@login_required
def task_delete(request, id):
        
        task = Task.objects.get(id=id)
        
        if task.author == request.user:
                if request.method == 'POST':
                        task.delete()
        return redirect('task')
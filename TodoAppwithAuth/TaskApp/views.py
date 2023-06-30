from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.

class TaskLoginView(LoginView):
    template_name = 'TaskApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('TaskView')

class TaskView(LoginRequiredMixin, ListView):
    model = Task
    #setting our user defined query set object name
    context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    #setting our user defined query set object name
    context_object_name = 'task'
    #setting our user defined template name
    template_name = 'TaskApp/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('TaskView')
    template_name = 'TaskApp/task_create.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('TaskView')
    template_name = 'TaskApp/task_update.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('TaskView')
    template_name = 'TaskApp/task_delete.html'


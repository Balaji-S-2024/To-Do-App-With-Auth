from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Task

# Create your views here.

class TaskLoginView(LoginView):
    template_name = 'TaskApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('TaskView')
    

class RegisterView(FormView):
    template_name = 'TaskApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('TaskView')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('TaskView')
        return super(RegisterView, self).get(*args, **kwargs)
    
    

class TaskView(LoginRequiredMixin, ListView):
    model = Task
    #setting our user defined query set object name
    context_object_name = 'tasks'
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user = self.request.user)
        context["count"] = context["tasks"].filter(complete = False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input :
            context["tasks"] = context["tasks"].filter(title__startswith = search_input)
        context['search_input'] = search_input

        return context



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    #setting our user defined query set object name
    context_object_name = 'task'
    #setting our user defined template name
    template_name = 'TaskApp/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('TaskView')
    template_name = 'TaskApp/task_create.html'

    #
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

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

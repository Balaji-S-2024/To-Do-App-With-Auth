from django.urls import path
from .views import TaskView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #when we use this url routing ({% url 'name=' modelname.pk %}) this name= in path funtions helps us 
    path('TaskLoginView', TaskLoginView.as_view(), name='TaskLoginView'),
    path('LogoutView', LogoutView.as_view(next_page = 'TaskLoginView'), name='LogoutView'),

    path('', TaskView.as_view(), name='TaskView'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='TaskDetail'),
    path('TaskCreate', TaskCreate.as_view(), name='TaskCreate'),
    path('TaskUpdate/<int:pk>/', TaskUpdate.as_view(), name='TaskUpdate'),
    path('TaskDelete/<int:pk>/', TaskDelete.as_view(), name='TaskDelete'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.indexPage, name='home'),
    path('hello/<str:username>', views.helloUser, name='hello'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('CreateTasks/',views.Create_Task, name='create_task'),
    path('CreateProject/', views.Create_Project, name='create_project')
    


]

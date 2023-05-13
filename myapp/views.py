from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def indexPage(request):
    return HttpResponse('Index Page')

def helloUser(request, username):
    print(username)
    return HttpResponse('Hello %s' % username)  

def about(request):
    return HttpResponse('About')

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('Tasks: %s' % task.title)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
    
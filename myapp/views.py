from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def helloUser(request, username):
    print(username)
    return HttpResponse('Hello %s' % username)  

def about(request):
    return render(request, 'About.html')

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('Tasks: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, "Task.html",  {'tasks': tasks})

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(request, "Projects.html",  {'projects': projects})
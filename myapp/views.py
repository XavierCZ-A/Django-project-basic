from django.shortcuts import render,  redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateTask, CreateProject
from django.shortcuts import get_object_or_404

# Create your views here.
def indexPage(request):
    return render(request, 'Index.html')

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

def Create_Task(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render(request, "Create_task.html", {'form': CreateTask(), 'projects': projects})
    else:
        project_id = request.POST['project']
        project = get_object_or_404(Project, id=project_id)

        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project = project)
        return redirect('tasks')
    
def Create_Project(request):
        if request.method == 'GET':
            return render(request, "Create_project.html", {'form': CreateProject()})
        else:
            Project.objects.create(name = request.POST['name'])
            return redirect('create_project')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPage(request):
    return HttpResponse('Index Page')

def helloUser(request, username):
    print(username)
    return HttpResponse('Hello %s' % username)  

def about(request):
    return HttpResponse('About')
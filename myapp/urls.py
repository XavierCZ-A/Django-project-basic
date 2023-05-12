from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.indexPage),
    path('hello/<str:username>', views.helloUser),
    path('about/', views.about),

]
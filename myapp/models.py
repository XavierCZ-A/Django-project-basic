from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)

class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

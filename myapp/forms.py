from django import forms


class CreateTask(forms.Form):
    title = forms.CharField(label='Title' ,max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class CreateProject(forms.Form):
    name = forms.CharField(label='Project name', max_length=200)
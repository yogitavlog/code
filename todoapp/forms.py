from django import forms
from django.forms import ModelForm
from todoapp.models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

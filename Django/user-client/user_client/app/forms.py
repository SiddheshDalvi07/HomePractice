# forms.py

from django import forms
from .models import Client, Project

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'client', 'users']
        widgets = {
            'users': forms.CheckboxSelectMultiple(),
        }

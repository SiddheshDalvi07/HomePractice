from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is a about page of app3")

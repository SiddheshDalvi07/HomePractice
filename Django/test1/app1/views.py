from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  index(request):
    return HttpResponse('hello world')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"index.html")

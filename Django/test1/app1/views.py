from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def  index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse("about page")

def contact(request):
    return render(request,"index.html")

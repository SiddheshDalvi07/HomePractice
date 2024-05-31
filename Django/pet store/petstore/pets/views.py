from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Pet

def expensive_pets(request):
    price_threshold = 5000
    pets = Pet.objects.filter(price__gt=price_threshold)
    return render(request, 'expensive_pets.html', {'pets': pets})
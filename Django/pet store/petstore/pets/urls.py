from django.urls import path
from .views import expensive_pets

urlpatterns = [
    path('expensive_pets/', expensive_pets, name='expensive_pets'),
]

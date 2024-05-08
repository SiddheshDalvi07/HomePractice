# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('media/', views.media_list, name='media_list'),
]

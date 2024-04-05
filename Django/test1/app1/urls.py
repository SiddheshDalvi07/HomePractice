from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("contact/about",views.about),
    path("about/",views.about),
    path("contact/",views.contact),
]
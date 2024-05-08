from django.urls import path
from . import views

urlpatterns = [
    path('empapp/empname/<str:lookup>/<str:search_string>/', views.employee_search_by_name),
    path('empapp/empage/<str:lookup>/<int:age>/', views.employee_search_by_age),
]
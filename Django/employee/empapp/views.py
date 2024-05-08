from django.shortcuts import render
from .models import Employee
# Create your views here.



def employee_search_by_name(request, lookup, search_string):
    if lookup == 'startswith':
        employees = Employee.objects.filter(fname__startswith=search_string)
    elif lookup == 'contains':
        employees = Employee.objects.filter(fname__contains=search_string)
    else:
        # Handle invalid lookup
        employees = None
    
    return render(request, 'employee_list.html', {'employees': employees})

def employee_search_by_age(request, lookup, age):
    if lookup == 'lte':
        employees = Employee.objects.filter(age__lte=age)
    else:
        # Handle invalid lookup
        employees = None
    
    return render(request, 'employee_list.html', {'employees': employees})
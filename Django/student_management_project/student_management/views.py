from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'age', 'grade']
    success_url = reverse_lazy('student_list')
    template_name = 'student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'age', 'grade']
    success_url = reverse_lazy('student_list')
    template_name = 'student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    template_name = 'student_confirm_delete.html'


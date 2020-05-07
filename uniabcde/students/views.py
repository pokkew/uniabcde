from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from .models import Student

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = [
        'name',
        'phone',
        'email',
        'art',
        'course',
    ]
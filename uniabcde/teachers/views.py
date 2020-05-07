
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from .models import Teacher
from django import forms

class DateInput(forms.Form):
    input_type = 'date'

class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherCreateView(CreateView):
    model = Teacher
    fields = [
        'name',
        'phone',
        'email',
        'salary',
        'course',
        'start_date',
    ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_date'].widget = forms.SelectDateWidget()
        return form
    


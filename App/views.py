from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from App.models import *

class SchoolList(ListView):
    model=School
    template_name='App/school_list.html'
    context_object_name='ASO'
    # queryset=School.objects.all()
    ordering=['id']

class StudentList(ListView):
    model=Student
    template_name='App/student_list.html'
    context_object_name='ASO'
    # queryset=Student.objects.all()
    ordering=['id']
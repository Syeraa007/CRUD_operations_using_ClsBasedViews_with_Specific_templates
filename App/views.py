from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from App.models import *

class SchoolList(ListView):
    model=School
    # template_name='App/school_list.html'
    # templates will be directly rendered by ListView implicitly
    context_object_name='ASO'
    # queryset=School.objects.all()
    ordering=['id']

class StudentList(ListView):
    model=Student
    # template_name='App/student_list.html'
    # templates will be directly rendered by ListView implicitly
    context_object_name='ASO'
    # queryset=Student.objects.all()
    ordering=['id']

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'
    # template_name='App/school_detail.html'
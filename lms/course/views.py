from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = 'all_courses'
    template_name = 'course/all_courses.html'
    
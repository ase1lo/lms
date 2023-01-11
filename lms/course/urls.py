from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_courses', CourseListView.as_view(), name='all_courses')

]
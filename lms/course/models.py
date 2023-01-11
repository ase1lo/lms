from django.db import models
from users.models import CustomUser
# Create your models here.



class Course(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT)


class Category(models.Model):
    category = models.CharField(max_length=100)


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    step = models.ForeignKey('Step', on_delete=models.PROTECT)


class Step(models.Model):
    step_text = models.TextField(max_length=1000)


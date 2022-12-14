from django.db import models
from django.utils import timezone

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)  
# спросить про юзера, чтобы не делать автора 
# про запросы через ?


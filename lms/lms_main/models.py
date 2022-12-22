from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    preview_text = models.TextField(max_length=100, blank=True)
    preview_text_from_topic = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return "http://127.0.0.1:8000/blog/topic_create"

# спросить про юзера, чтобы не делать автора 
# про запросы через ?
# get_abs_url
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('all_topics/', TopicListView.as_view(), name = 'all_topics'),
    path('topic_create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic_detail/<int:pk>', TopicDetailView.as_view(), name='topic_detail'),
    path('topics_by_category/<str:category>', TopicByCategory.as_view(), name='topics_by_category'),
    path('topic_update/<int:pk>', TopicUpdateView.as_view(), name='topic_update'),
    path('topic_delete/<int:pk>', TopicDeleteView.as_view(), name='topic_delete'),
    path('home/', blog_home, name='blog_home')
]
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import TopicForm
from django.http import Http404

# Create your views here.

class TopicListView(ListView):
    model = Topic
    context_object_name = 'all_topics'
    template_name = 'blog/all_topics.html'


class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topic/topic_form.html'

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic/topic_detail.html'
    context_object_name = 'topic'


class TopicByCategory(ListView):
    model = Topic
    template_name = 'blog/get_topics_by_category'
    context_object_name = "topics_by_category"

    def get(self, request, *args, **kwargs): # blog/topic_byt_category/Python - Python (конец url) - получаем из
        request_category = kwargs['category']  # из метода get 
        try:
            self.category_id = Category.objects.get(title=request_category).id
        except:
            raise Http404("Url does not exist") 
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['topics_by_category'] = Topic.objects.filter(category=self.category_id)
        return data


def blog_home(request):
    return render(request, 'blog/blog_home.html') 
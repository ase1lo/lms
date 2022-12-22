from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Category, Topic



class TopicForm(forms.ModelForm):
    is_published = forms.CheckboxInput(
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Категория',
        widget=forms.Select({'class': 'form-control'})
    )
    

    class Meta:
        model = Topic
        exclude = []
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            

        }




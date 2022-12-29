from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'), 
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='profile'),
    path('profile/<int:author_id>/follow', views.follow, name='follow'),
    path('profile/<int:author_id>/unfollow', views.unfollow, name='unfollow'),
    ]

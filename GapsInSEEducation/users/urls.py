from django.urls import path
from . import views

# This file contains all of the url path names that are used throughout my project
app_name = 'users'
urlpatterns = [
    # path('', views.e7builds_build_home, name='e7builds_build_home'),
    path('register', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]

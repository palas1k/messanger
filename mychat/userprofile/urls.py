from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import SignUpView
from django.contrib.auth import logout

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('login/', LoginView.as_view(template_name = 'userprofile/login.html'), name = 'login'),
    path('logout/', logout, name = 'logout'),
]

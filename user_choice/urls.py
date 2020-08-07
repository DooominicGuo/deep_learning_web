from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_action, name='login'),
    path('register', views.register_action, name='register'),
    path('choosing_section', views.choosing_section, name='choose'),
    path('ending', views.ending, name = 'ending')
]
# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('study/', views.study, name='study'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('mentors/', views.mentors, name='mentors'),
    path('investors/', views.investors, name='investors'),
]

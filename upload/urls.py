from django.urls import path
from . import views

urlpatterns = [
    path('pdf', views.index, name='pdf'),
    path('word', views.word, name='word'),
]
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for heroes index
    path('heroes/', views.heroes_index, name='index'),
]
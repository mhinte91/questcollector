from django.shortcuts import render
from .models import Hero


# Create your views here.

def heroes_index(request):
    heroes = Hero.objects.all()
    return render(request, 'heroes/index.html', { 'heroes': heroes })

def home(request):
    return HttpResponse('<h1>Greetings, Adventurer</h1>')

def about(request):
    return render(request, 'about.html')
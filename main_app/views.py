from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hero
from .forms import EquipmentForm


# Create your views here.

class HeroDelete(DeleteView):
    model = Hero
    success_url = '/heroes/'

class HeroUpdate(UpdateView):
    model = Hero
    fields = ['hero_class', 'description', 'level']

class HeroCreate(CreateView):
    model = Hero
    fields = '__all__'

def heroes_detail(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    equipment_form = EquipmentForm()
    return render(request, 'heroes/detail.html', {
        'hero': hero,
        'equipment_form': equipment_form 
    })

def add_equipment(request, hero_id):
    form = EquipmentForm(request.POST)
    if form.is_valid():
        new_equipment = form.save(commit=False)
        new_equipment.hero_id = hero_id
        new_equipment.save()
    return redirect('detail', hero_id=hero_id)

def heroes_index(request):
    heroes = Hero.objects.all()
    return render(request, 'heroes/index.html', { 'heroes': heroes })

def home(request):
    return HttpResponse('<h1>Greetings, Adventurer</h1>')

def about(request):
    return render(request, 'about.html')
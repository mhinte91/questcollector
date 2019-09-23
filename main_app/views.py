from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hero, Quest, Photo
from .forms import EquipmentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'questcollector'

import uuid
import boto3



# Create your views here.

class HeroDelete(LoginRequiredMixin, DeleteView):
    model = Hero
    success_url = '/heroes/'

class HeroUpdate(LoginRequiredMixin, UpdateView):
    model = Hero
    fields = ['hero_class', 'description', 'level']

class HeroCreate(LoginRequiredMixin, CreateView):
    model = Hero
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def heroes_detail(request, hero_id):
    hero = Hero.objects.get(id=hero_id)
    quests_hero_doesnt_have = Quest.objects.exclude(id__in = hero.quests.all().values_list('id'))
    equipment_form = EquipmentForm()
    return render(request, 'heroes/detail.html', {
        'hero': hero,
        'equipment_form': equipment_form,
        'quests': quests_hero_doesnt_have
    })

@login_required
def add_equipment(request, hero_id):
    form = EquipmentForm(request.POST)
    if form.is_valid():
        new_equipment = form.save(commit=False)
        new_equipment.hero_id = hero_id
        new_equipment.save()
    return redirect('detail', hero_id=hero_id)

def heroes_index(request):
    heroes = Hero.objects.filter(user=request.user)
    return render(request, 'heroes/index.html', { 'heroes': heroes })

def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

class QuestList(LoginRequiredMixin, ListView):
  model = Quest

class QuestDetail(LoginRequiredMixin, DetailView):
  model = Quest

class QuestCreate(LoginRequiredMixin, CreateView):
  model = Quest
  fields = '__all__'

class QuestUpdate(LoginRequiredMixin, UpdateView):
  model = Quest
  fields = ['name', 'color']

class QuestDelete(LoginRequiredMixin, DeleteView):
  model = Quest
  success_url = '/quests/'

@login_required
def assoc_quest(request, hero_id, quest_id):
  # Note that you can pass a toy's id instead of the whole object
  Hero.objects.get(id=hero_id).quests.add(quest_id)
  return redirect('detail', hero_id=hero_id)

@login_required
def add_photo(request, hero_id):
# photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to hero_id or cat (if you have a cat object)
            photo = Photo(url=url, hero_id=hero_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', hero_id=hero_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
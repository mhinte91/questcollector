from django.shortcuts import render
from django.http import HttpResponse


class Hero:
    def __init__(self, name, hero_class, description, level):
        self.name = name
        self.hero_class = hero_class
        self.description = description
        self.level = level

heroes = [
    Hero('Merik', 'Fighter', 'Half-Orc steet-urchin with red hair, carries a steel glaive', 12),
    Hero('Frog', 'Druid', 'Tabaxi shapeshifter, obsessed with ancient artifacts', 11 ),
    Hero('Tekken', 'Monk', 'From parts unkown, faithful to his secret order', 13),
    Hero('Edward Hamilton', 'Bard', 'Entreprenuer and performer, interested in expanding his assets', 12),
    Hero('Kersit', 'Ranger', 'Explorer and Sailor, travels the world in search of lost maps of forgotten ruins', 13 )
]

# Create your views here.


def home(request):
    return HttpResponse('<h1>Greetings, Adventurer</h1>')

def about(request):
    return render(request, 'about.html')

def heroes_index(request):
    return render(request, 'heroes/index.html', {'heroes': heroes})
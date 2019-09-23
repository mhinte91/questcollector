from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

TYPE = (
    ('W', 'Weapon'),
    ('A', 'Armor'),
    ('M', 'Magic Item')
)

DIFFICULTY = (
    ('E', 'Easy'),
    ('H', 'Heroic'),
    ('L', 'Legendary')
)

class Quest(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[1][0]
    )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('quests_detail', kwargs={'pk': self.id})

class Hero(models.Model):
    name = models.CharField(max_length=100)
    hero_class = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    level = models.IntegerField()
    quests = models.ManyToManyField(Quest)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hero_id': self.id})

class Equipment(models.Model):
    name = models.CharField('Equipment Name', max_length=100)
    description = models.TextField('Equipment Description', max_length=2000)
    type = models.CharField(
        'Equipment Type',
        max_length=1,
        choices=TYPE,
        default=TYPE[0][0] 
        )
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_type_display()} Equipment: {self.name}'

class Photo(models.Model):
    url = models.CharField(max_length=200)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for hero_id: {self.hero_id} @{self_url}"

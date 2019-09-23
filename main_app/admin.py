from django.contrib import admin

from .models import Hero, Equipment, Quest, Photo

# Register your models here.

admin.site.register(Hero)
admin.site.register(Equipment)
admin.site.register(Quest)
admin.site.register(Photo)

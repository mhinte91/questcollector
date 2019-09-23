from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('heroes/', views.heroes_index, name='index'),
    path('heroes/<int:hero_id>/', views.heroes_detail, name='detail'),
    path('heroes/create/', views.HeroCreate.as_view(), name='heroes_create'),
    path('heroes/<int:pk>/update', views.HeroUpdate.as_view(), name='heroes_update'),
    path('heroes/<int:pk>/delete', views.HeroDelete.as_view(), name='heroes_delete'),
    path('heroes/<int:hero_id>/add_equipment/', views.add_equipment, name='add_equipment'),
    path('heroes/<hero_id>/add_photo', views.add_photo, name='add_photo'),
    path('heroes/<int:hero_id>/assoc_quest/<int:quest_id>/', views.assoc_quest, name='assoc_quest'),
    path('quests/', views.QuestList.as_view(), name='quests_index'),
    path('quests/<int:pk>/', views.QuestDetail.as_view(), name='quests_detail'),
    path('quests/create/', views.QuestCreate.as_view(), name='quests_create'),
    path('quests/<int:pk>/update/', views.QuestUpdate.as_view(), name='quests_update'),
    path('quests/<int:pk>/delete/', views.QuestDelete.as_view(), name='quests_delete'),
    path('accounts/signup', views.signup, name='signup'),
]
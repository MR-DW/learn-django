# Django import
from django.urls import path 
from . import views

# Views
from heroe.views import HeroApiView, CreateHeroApiView, HeroDetailApiView

# Urls
urlpatterns = [
    path('', views.Index, name='home'),
    path('lista-heroes/', views.lista, name='lista'),
    path('crear-heroe/', views.crear, name='custom'),
    path('eliminar-heroe/', views.delete, name='delete'),
    
    path('heroes-list/', HeroApiView.as_view(), name='heroes_list'),
    path('create-heroe/', CreateHeroApiView.as_view(), name='create_heroe'),
    path('detail-heroe/<int:pk>/', HeroDetailApiView.as_view(), name='detail'),
    
    
]






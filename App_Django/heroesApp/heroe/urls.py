# Django import
from django.urls import path 



# Views
from heroe.views import HeroApiView, CreateHeroApiView, HeroDetailApiView

# Urls
urlpatterns = [
    path('heroes-list/', HeroApiView.as_view(), name='heroes_list'),
    path('create-heroe/', CreateHeroApiView.as_view(), name='create_heroe'),
    path('detail-heroe/<int:pk>/', HeroDetailApiView.as_view(), name='detail'),
    
]






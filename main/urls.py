from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('persons_list', views.persons_list, name='persons_list'),
    # path('greet', views.greet, name='greet'),
    path('config', views.config, name='config'),
    path('clear', views.config, name='clear'),
]


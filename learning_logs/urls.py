from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atividades', views.atividades, name='atividades'),
    path('anotacoes/<id_topic>/', views.anotacoes, name = 'anotacoes'),
    path('new_topic', views.new_topic, name = 'new_topic'),
    path('new_entry/<id_topic>/', views.new_entry, name= 'new_entry'),
]
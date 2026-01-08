from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atividades', views.atividades, name='atividades'),
    path('anotacoes/<id_topic>/', views.anotacoes, name = 'anotacoes')
]
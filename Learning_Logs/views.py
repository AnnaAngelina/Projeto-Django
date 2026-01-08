from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def atividades(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/atividades.html', context)

def anotacoes(request, id_topic):
    topic = Topic.objects.get(id = id_topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/anotacoes_topics.html', context)
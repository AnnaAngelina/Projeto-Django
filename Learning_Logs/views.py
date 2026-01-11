from django.shortcuts import render
from .models import Topic
from .forms import Topicform, Entryform
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def new_topic(request):
    if request.method != 'POST':
        form = Topicform()
    else:
        form = Topicform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, id_topic):
    topic = Topic.objects.get(id = id_topic)
    if request.method != 'POST':
        form = Entryform()
    else:
        form = Entryform(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('anotacoes', args=[id_topic]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

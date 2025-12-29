from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def atividades(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/atividades.html', context)
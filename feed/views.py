
import datetime
from multiprocessing import context
from django.shortcuts import render
from feed.models import Message
from django.http import HttpResponse

# Create your views here.
def index(request):
    #ajout d'une condition
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        Message.objects.create(content=content, user=user)
    context = {}
    context['messages'] = Message.objects.order_by('-created_at') # Ordonner les messages par heure plus recente
    return render(request, 'index.html', context=context)


def details(request, id):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        Message.objects.create(content=content, user=user, reponse_to_id=id)
        
    context = {}
    context['message'] = Message.objects.get(id=id)
    context['comments'] = Message.objects.filter(reponse_to=id)
    return render(request, 'details.html', context=context)
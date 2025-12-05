
import datetime
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'messages':[
            {
                'content': 'text',   # Pour le contenu du meassage
                'username': 'sanogo', # Pour le nom de l'utilisateur
                'created_at': datetime.datetime.now(),  # Pour la date de creation du message  
            },
            {
                'content': 'text',   # Pour le contenu du meassage
                'username': 'sanogo', # Pour le nom de l'utilisateur
                'created_at': datetime.datetime.now(),  # Pour la date de creation du message  
            },
            {
                'content': 'text',   # Pour le contenu du meassage
                'username': 'sanogo', # Pour le nom de l'utilisateur
                'created_at': datetime.datetime.now(),  # Pour la date de creation du message  
            }
        ]
    }
    return render(request, 'index.html', context=context)
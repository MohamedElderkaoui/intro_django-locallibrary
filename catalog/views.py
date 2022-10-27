from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texto = '''<h1>LibrerÃ­a Local</h1>
    <p>Esta es la pÃ¡gina principal de la librerÃ­a local.</p>'''
    # texto = 'PÃ¡gina inicial de la librerÃ­a local'
    return HttpResponse(texto)

def acerca_de(request):
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pÃ¡gina de acerca de de la librerÃ­a local.</p>
    <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python logo">
    
    '''
    return HttpResponse(texto)




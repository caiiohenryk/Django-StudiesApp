from django.shortcuts import render
from django.http import HttpResponse

"""
 Criando a primeira view pra testar
"""

def index(request):
    return HttpResponse("Essa é a página inicial... Meu projeto está indo bem!")
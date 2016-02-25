from django.shortcuts import render
from django.core.urlresolvers import reverse

def cenario(request):
    return render(request,'treinamento/cenario.html',{})

def usuarios(request):
    return render(request,'treinamento/usuarios.html',{})
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('treinamento:cenario'))

def cenario(request):
    return render(request,'treinamento/cenario.html',{})

def usuarios(request):
    return render(request,'treinamento/usuarios.html',{})
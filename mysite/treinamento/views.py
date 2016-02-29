from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    return HttpResponseRedirect(reverse('treinamento:cenario'))

def cenario(request):
    return render(request,'treinamento/cenario.html',{})

def usuarios(request):
    return render(request,'treinamento/usuarios.html',{})

def rest_agent(request,agent_id = None):
    if agent_id == None:
        #get all agents
        if request.method == "GET":
            return rest_agent_get_all(request)
        #add agent
        elif request.method == "POST":
            return rest_agent_add(request)
        #Method not allowed 405
        else:
            return HttpResponse(status=405)
    elif request.method == "GET":
        #get agent by id
        return rest_agent_get(request,agent_id)
    elif request.method == "PUT":
        #update agent
        return rest_agent_update(request,agent_id)
    elif request.method == "DELETE":
        #delete agent
        return rest_agent_delete(request,agent_id)
    else:
        #Method not allowed
        return HttpResponse(status=405)

def rest_agent_get(request,agent_id):
    return HttpResponse(status=405)

def rest_agent_get_all(request):
    return HttpResponse(status=405)

def rest_agent_add(request):
    return HttpResponse(status=405)

def rest_agent_update(request,agent_id):
    return HttpResponse(status=405)

def rest_agent_delete(request,agent_id):
    return HttpResponse(status=405)
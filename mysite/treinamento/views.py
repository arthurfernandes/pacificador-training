import simplejson
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.db import IntegrityError
from .models import Agent

def index(request):
    return HttpResponseRedirect(reverse('treinamento:cenario'))

def cenario(request):
    return render(request,'treinamento/cenario.html',{})

def usuarios(request):
    return render(request,'treinamento/usuarios.html',{})

@csrf_exempt
def rest_agent(request,agent_id = None):
    #Bad Request
    if isinstance(agent_id,(int,long)):
        return HttpResponse(status = 400)
    elif agent_id is None:
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
    agent = get_object_or_404(Agent,pk = agent_id)
    data = agent.to_json()
    return HttpResponse(data,status=200,content_type='application/json')

def rest_agent_get_all(request):
    agents = Agent.objects.all()
    data = '[' + ','.join(agent.to_json() for agent in agents) + ']'
    return HttpResponse(data,content_type='application/json')

def rest_agent_add(request):
    #Works only with post requests
    if request.method != 'POST':
        #Internal Server Error
        return HttpResponse(status = 500)
    else:
        #Getting data from Post Request
        params = request.POST
        name = params.get('name',default=None)
        lat = params.get('lat',default=None)
        lon = params.get('lon',default=None)

        if name is None:
            return HttpResponse(status = 400)
        else:
            agent = Agent(name = name)
            try:
                agent.lat = int(lat) if (lat is not None) else None
                agent.lon = int(lon) if (lon is not None) else None
                agent.save()
            except ValueError,IntegrityError:
                #Validation error in Model Constraints
                return HttpResponse(status = 400)
            except:
                return HttpResponse(status = 500)

            response = HttpResponse(status = 201)
            response['Location'] = request.build_absolute_uri() + ("/%d" % agent.id)
            return response

def rest_agent_update(request,agent_id):
    #Retrieving object
    agent = get_object_or_404(Agent,pk=agent_id)

    #Getting data from Put Request
    params = QueryDict(request.body)
    name = params.get('name',default=None)
    lat = params.get('lat',default=None)
    lon = params.get('lon',default=None)

    if name is None:
        return HttpResponse(status = 400)

    try:
        agent.name = name
        agent.lat = int(lat) if (lat is not None) else None
        agent.lon = int(lon) if (lon is not None) else None
        agent.save()
    except ValueError,IntegrityError:
        #Validation error in Model Constraints
        return HttpResponse(status = 400)
    except:
        return HttpResponse(status = 500)

    return HttpResponse(status = 200)

def rest_agent_delete(request,agent_id):
    #Retrieving object
    agent = get_object_or_404(Agent,pk=agent_id)

    try:
        agent.delete()
    except:
        return HttpResponse(status = 500)

    return HttpResponse(status = 200)

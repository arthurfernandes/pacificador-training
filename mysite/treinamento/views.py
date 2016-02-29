from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from utils.http import JsonHttpResponse, list_to_json
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
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
    #TODO
    return HttpResponse(status = 404)
    # return JsonHttpResponse({"id":agent.id,"name":agent.name,"lat":agent.lat,"lon":agent.lon},200)

def rest_agent_get_all(request):
    agents = Agent.objects.all()
    if agents is not None:
        data = serializers.serialize('json',agents)
        #TODO
        return HttpResponse(data,content_type='application/json')
    else:
        #Internal Server Error
        return HttpResponse(status = 500)

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
            agent = Agent(name = name, lat=lat, lon=lon)
            try:
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

    #Getting data from Post Request
    params = request.POST
    name = params.get('name',default=None)
    lat = params.get('lat',default=None)
    lon = params.get('lon',default=None)

    if name is None:
        return HttpResponse(status = 400)

    agent.name = name
    agent.lat = lat
    agent.lon = lon
    try:
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

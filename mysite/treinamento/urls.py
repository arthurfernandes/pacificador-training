from django.conf.urls import url
from .import views

app_name = 'treinamento'

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^cenario$', views.cenario, name = 'cenario'),
    url(r'^usuarios$',views.usuarios, name='usuarios'),
    url(r'^rest/agent/(?P<agent_id>[0-9]+)',views.rest_agent,name='rest_agent'),
    url(r'^rest/agent',views.rest_agent,name='rest_agent')
]

from django.conf.urls import url
from .import views

app_name = 'treinamento'

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^cenario$', views.cenario, name = 'cenario'),
    url(r'^usuarios$',views.usuarios, name='usuarios'),
]

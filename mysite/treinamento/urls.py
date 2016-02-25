from django.conf.urls import url
from .import views

app_name = 'treinamento'

urlpatterns = [
    url(r'^$', views.cenario, name = 'cenario'),
]

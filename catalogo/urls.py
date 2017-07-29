# Catalogo URLS

from django.conf.urls import url
from catalogo import views

urlpatterns = [
    url(r'^$', "catalogo.views.catalogo_home"),   
    url(r'^(?P<id>\d+)/', "catalogo.views.detalhe_do_post", name="detalhe"),
    url(r'^lista/', "catalogo.views.lista_de_posts"),
]

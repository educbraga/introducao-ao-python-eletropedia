from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    imagem = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    titulo = models.CharField(max_length=120)
    conteudo = models.TextField()
    atualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicorde__(self):
        return self.titulo
        
    def __str__(self):
        return self.titulo
        
    def get_absolute_url(self):
        return reverse("detalhe", kwargs = {"id": self.id})
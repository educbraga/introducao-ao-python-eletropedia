from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["titulo", "atualizado", "timestamp"]
    list_display_links = ["atualizado"]
    list_editable = ["titulo"]
    list_filter = ["atualizado", "timestamp"]
    search_fields = ["titulo", "conteudo"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
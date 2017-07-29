from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def catalogo_home(request):
    context = {
        
    }
    return render(request,"home.html", context)
    
def detalhe_do_post(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post,
    }
    return render(request,"detalhe.html", context)

def lista_de_posts(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5) # Show 5 contacts per page

    page = request.GET.get('pagina')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    context = { 
        "posts": queryset,
    }
    return render(request,"lista.html", context)
    
    
def listing(request):
    contact_list = Contacts.objects.all()


    return render(request, 'list.html', {'contacts': contacts})
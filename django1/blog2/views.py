from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request,'blog2/index.html',{'article':article})

def list(request):
    articles = models.Article.objects.all();
    return render(request,'blog2/list.html',{'articles':articles})

def article_page(request,article_id):
    article = module.Article.object.get(pk = article_id)
    return  render(request,'blog2/article_page.html',{'article':article })

from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.db import connection,transaction



# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from .models import Blog, BlogAdmin, Author

cursor = connection.cursor()

def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})



class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class HomePageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.raw('select * from Blog')
        return context
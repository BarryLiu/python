from django.shortcuts import render
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("hello world")

def index(request):
    return  render(request,"blog/index.html")


def index2(request):
    return render(request,"blog/index2.html",{'hello':'你好，世界！！！'})
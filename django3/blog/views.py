from django.shortcuts import render, render_to_response

# Create your views here.
from .models import Book


def index(request):
    book_list = Book.objects.all()
    return render_to_response('index.html',{'books':book_list})
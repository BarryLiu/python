from django.urls import path
from . import views


urlpatterns = [
    path('helloworld/', views.helloworld),
    path('',views.index),
    path('index/',views.index),
    path('index2/',views.index2),
]

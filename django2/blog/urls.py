from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    # path('article/(?P<article_id>[0-9]+)/$',views.article_page),

]

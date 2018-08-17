from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('',views.index),
    path('index/',views.index),#普通方法调用
    # path('article/(?P<article_id>[0-9]+)/$',views.article_page),
    path('helloview', views.MyView.as_view(), name='my-view'), #基础view页面
    path('baidu', RedirectView.as_view(url='http://baidu.com'), name='baidu'),#重定向
]

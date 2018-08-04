"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as vb

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', vb.index),
    path('helloworld/', vb.helloworld),# url 引用方式1

    path('blog/', include('blog.urls')),# url 引用方式2
    path('blog2/', include('blog2.urls')),# url 引用方式2

]

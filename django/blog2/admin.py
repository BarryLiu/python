from django.contrib import admin

from .models import Article

# Register your models here.
# 注册 到admin模块管理
admin.site.register(Article)
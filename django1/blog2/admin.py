from django.contrib import admin

from .models import Article
from .models import Test,Contact,Tag
# Register your models here.
# 注册 到admin模块管理
admin.site.register(Article)

admin.site.register([Test, Contact, Tag])
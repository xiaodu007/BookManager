from django.contrib import admin
from Book.models import BookInfo,People

# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    """人物信息模型站点管理类"""
    list_display = ['id','gender','name','book']


# 注册书籍信息模型类
admin.site.register(BookInfo)
# 注册人物信息模型类
admin.site.register(People,PeopleAdmin)
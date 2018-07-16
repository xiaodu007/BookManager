"""BookManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # http://127.0.0.1:8000/admin
    # 正则匹配，对请求地址进行正则匹配，如果路径中包含‘admin/’,就把后台站点中的urls信息包含到项目中，指明下一级目录应该如何匹配
    url(r'^admin/', include(admin.site.urls)),
    # http://127.0.0.1:8000/
    # 正则匹配，对请求地址进行正则匹配，如果路径中不包含‘admin/’,就把Book应用中的urls信息包含到项目中，指明下一级目录应该如何匹配
    url(r'^', include('Book.urls'))
]



from django.conf.urls import include, url
from Book.views import test,bookList,peopleList

urlpatterns = [
    # http://127.0.0.1:8000/test
    # 正则匹配，对请求地址进行正则匹配，如果路径不包含‘test/’,就把Book应用中的urls信息包含到项目中，指明下一级目录应该如何匹配
    url(r'^test/$', test),
    url(r'^booklist/$', bookList),
    url(r'^(\d+)/$', peopleList)

]
from django.shortcuts import render
from django.http import HttpResponse
from Book.models import BookInfo,People
# Create your views here.


def peopleList(request,book_id):
    """人物信息列表"""
    book = BookInfo.objects.get(id=book_id)
    people_list = book.people_set.all()
    context = {
        'people_list': people_list
    }
    return render(request, 'Book/peoplelist.html', context)


def bookList(request):
    """书籍信息列表"""
    book_list = BookInfo.objects.all();
    context = {
        'book_list': book_list
    }

    return render(request,'Book/booklist.html',context)


def test(request):
    """测试：测试路径的配置"""
    # return HttpResponse('测试')

    # 调用模板并响应: 未接收参数
    # return render(request, 'Book/test.html')

    # 调用模板但是有参数，上下文，一般是从数据库中查找出的数据
    context = {
        'test': '测试'
    }
    return render(request,'Book/test.html',context)
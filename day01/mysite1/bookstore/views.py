import time

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from bookstore.models import Book
# 整体缓存
from django.views.decorators.cache import cache_page
# 局部缓存
from django.core.cache import cache


# Create your views here.

def all_book(request):
    book = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('Exception is ', e)
        return HttpResponse('The book is not exist! ')
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']
        # 修改数据
        if price:
            book.price = price
        if market_price:
            book.market_price = market_price
        # 保存数据库
        book.save()

        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    book_id = request.GET.get('book_id')
    print('book_id------------>', book_id)
    if not book_id:
        return HttpResponse('--请求异常')
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('the error is ', e)
        return HttpResponse('--the book id is error')

    # 伪删除
    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')


@cache_page(5)
def cache_view(request):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    a = time.strptime(t, '%Y-%m-%d %H:%M:%S')
    res = t + '&nbsp;&nbsp;' + str(int(time.mktime(a)))
    # num = int(time.mktime(a))
    # t_tuple = time.localtime(num)
    print(11111111, res)
    return HttpResponse(res)

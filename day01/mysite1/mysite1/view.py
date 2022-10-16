from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

POST_FORM = '''
<form method='post' action='/test_get_post'>
    用户名:<input type='text' name='username'>
    <input type='submit' value='提交'>
</form>
'''


def index_view(request):
    html = '这是我的首页'
    print(html)
    return HttpResponse(html)


def page1_view(request):
    html = '这是编号为1的网页'
    return HttpResponse(html)


def page2_view(request):
    html = '这是编号为2的网页'
    return HttpResponse(html)


def pagen_view(request, pg):
    html = '这是编号为%d的网页' % pg
    return HttpResponse(html)


def result_view(request, n, op, m):
    if op not in ['add', 'sub', 'mul']:
        html = 'op 不在指定范围内！'
        return HttpResponse(html)
    result = 0
    if op == 'add':
        result = n + m
    elif op == 'sub':
        result = n - m
    elif op == 'mul':
        result = n * m
    html = '结果为: %d' % result
    return HttpResponse(html)


def birthday_view(request, y, m, d):
    html = '日期为%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)


def test_request(request):
    print('#######################')
    print('path_info is ' + request.path_info)
    print('method is ' + request.method)
    print('GET is ', request.GET)
    print('全地址为 ： ' + request.get_full_path())
    print('session is ： ', request.session)
    print('COOKIES is ： ', request.COOKIES)
    print('body is ： ', request.body)

    return HttpResponse('test_request OK!')


def test_get_post(request):
    if request.method == 'GET':
        print('##############')
        print('GET is ', request.GET)
        print(request.GET.get('a', 'no a'))
        print(request.GET.get('c', 'no c'))
        print(request.GET.getlist('a'))
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        print('POST is ', request.POST)
        print('username is ', request.POST['username'])
        return HttpResponse('post is ok')
    else:
        pass

    return HttpResponse()


def test_html(request):
    # # 方案一
    # from django.template import loader
    # t = loader.get_template('test_html.html')
    # html = t.render()     # 把t对象转为字符串
    # return HttpResponse(html)

    # 方案二
    from django.shortcuts import render
    dic = {
        'username': 'Saber',
        'subject': ['math', 'English', 'computer'],
        'score': {'A': 84, 'B': 121},
        'age': 25
    }
    return render(request, 'test_html.html', dic)


def mycal(request):
    # print('11111->request.method:', request.method, type(request.method))
    if request.method == 'GET':
        return render(request, 'mycal.html')
    if request.method == 'POST':
        print('2222->request.method:', request.method, type(request.method))
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']

        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        print(1111111111111, locals())
        return render(request, 'mycal.html', locals())


def base_html(request):
    username = 'Saber'
    return render(request, 'base_html.html', locals())


def music_html(request):
    return render(request, 'music.html')


def sport_html(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def url_result(request):
    return HttpResponse('~~url_result is ok')


def url_result_n(request, pg):
    return HttpResponse('~~url_result_n is ok')


def url_reverse(request):
    from django.urls import reverse
    url = reverse('base')
    return HttpResponseRedirect(url)


def test_static(request):
    return render(request, 'test_static.html')

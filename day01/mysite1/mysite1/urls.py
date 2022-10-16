"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index_view),
    # http://127.0.0.1:8000/page/1
    path('page/1', view.page1_view),
    path('page/2', view.page2_view),
    path('page/<int:pg>', view.pagen_view),
    path('<int:n>/<str:op>/<int:m>', view.result_view),
    # http://127.0.0.1:8000/birthday/年4/月2/天2
    re_path('^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$', view.birthday_view),
    path('test_request', view.test_request),
    path('test_get_post', view.test_get_post),
    path('test_html', view.test_html),
    path('mycal', view.mycal),
    path('base', view.base_html, name='base'),
    path('music', view.music_html),
    path('sport', view.sport_html),
    path('test/url', view.test_url),
    path('test/url_result', view.url_result, name='ur'),
    path('test/url_result/<int:pg>', view.url_result_n, name='ur_p'),
    path('test/url_reverse', view.url_reverse, name='reverse'),
    path('test_static', view.test_static),
    # 分布式路由，后'/'必须加
    path('bookstore/', include('bookstore.urls'))
]

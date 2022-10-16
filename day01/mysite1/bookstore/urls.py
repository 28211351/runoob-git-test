from django.urls import path
from . import views

# path 全部在 http://127.0.0.1:8000/bookstore/  路由地址下
urlpatterns = [
    # http://127.0.0.1:8000/bookstore/all_book
    path('all_book', views.all_book),
    # http://127.0.0.1:8000/bookstore/update_book/1
    path('update_book/<int:book_id>', views.update_book),
    path('delete_book', views.delete_book),
    path('cache_view', views.cache_view),
]
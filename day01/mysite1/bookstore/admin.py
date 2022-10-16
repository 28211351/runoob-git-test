from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookManager(admin.ModelAdmin):
    # admin后台页面配置
    # 页面显示的哪些字段
    list_display = ['id', 'title', 'pub', 'price']
    # 设定页面哪个字段可链接到更改页面
    list_display_links = ['title', 'id']
    # 添加页面过滤器
    list_filter = ['pub']
    # 启用搜索框
    search_fields = ['title', 'id']
    # 允许页面字段编辑修改
    list_editable = ['price']


class AuthorManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_editable = ['age']



admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)


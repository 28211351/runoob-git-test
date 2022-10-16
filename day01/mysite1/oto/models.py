from django.db import models


# Create your models here.

# 一对一， 一对多， 多对多

class Author(models.Model):
    name = models.CharField('姓名', max_length=11)


class Wife(models.Model):
    name = models.CharField('姓名', max_length=11)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Pub(models.Model):
    name = models.CharField('出版社', max_length=50)


class Book(models.Model):
    name = models.CharField('图书', max_length=11)
    pubs = models.ManyToManyField(Pub)





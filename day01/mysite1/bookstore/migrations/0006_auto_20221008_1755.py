# Generated by Django 3.2.15 on 2022-10-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_alter_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='info',
        ),
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='零售价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=100, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=50, unique=True, verbose_name='书名'),
        ),
        migrations.AlterModelTable(
            name='author',
            table='tbl_author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='tbl_book',
        ),
    ]

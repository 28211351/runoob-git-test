# Generated by Django 3.2.15 on 2022-10-11 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='出版社')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='图书')),
                ('pubs', models.ManyToManyField(to='oto.Pub')),
            ],
        ),
    ]

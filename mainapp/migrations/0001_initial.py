# Generated by Django 4.1.3 on 2022-11-15 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста')),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_posts/')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('in_archive', models.BooleanField(default=False)),
                ('blog_category',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.blogcategory',
                                   verbose_name='Имя категории')),
            ],
        ),
    ]

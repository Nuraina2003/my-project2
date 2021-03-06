# Generated by Django 4.0.3 on 2022-04-14 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категориялар',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=255)),
                ('mather_name', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистрация',
            },
        ),
        migrations.CreateModel(
            name='arts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тақырып')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Сурет')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Құрылған уақыт')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Өзгертілген уақыт')),
                ('is_published', models.BooleanField(default=True, verbose_name='Шығарылым')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arts.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Өнер ',
                'verbose_name_plural': 'Өнер адамдары',
                'ordering': ['title', 'photo'],
            },
        ),
    ]

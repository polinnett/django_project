# Generated by Django 4.2.2 on 2023-06-24 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('proteins', models.IntegerField(verbose_name='Белки')),
                ('fats', models.IntegerField(verbose_name='Жиры')),
                ('carbohydrates', models.IntegerField(verbose_name='Углеводы')),
            ],
            options={
                'verbose_name': 'Фрукт',
                'verbose_name_plural': 'Фрукты',
            },
        ),
        migrations.CreateModel(
            name='Grain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('proteins', models.IntegerField(verbose_name='Белки')),
                ('fats', models.IntegerField(verbose_name='Жиры')),
                ('carbohydrates', models.IntegerField(verbose_name='Углеводы')),
            ],
            options={
                'verbose_name': 'Крупа',
                'verbose_name_plural': 'Крупы',
            },
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('proteins', models.IntegerField(verbose_name='Белки')),
                ('fats', models.IntegerField(verbose_name='Жиры')),
                ('carbohydrates', models.IntegerField(verbose_name='Углеводы')),
            ],
            options={
                'verbose_name': 'Мясо',
                'verbose_name_plural': 'Мясо',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('height', models.IntegerField(verbose_name='Рост')),
                ('weight', models.IntegerField(verbose_name='Вес')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('reg_date', models.DateField(default=django.utils.timezone.now)),
                ('user_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('calories', models.IntegerField(verbose_name='Калории')),
                ('proteins', models.IntegerField(verbose_name='Белки')),
                ('fats', models.IntegerField(verbose_name='Жиры')),
                ('carbohydrates', models.IntegerField(verbose_name='Углеводы')),
            ],
            options={
                'verbose_name': 'Овощ',
                'verbose_name_plural': 'Овощи',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_id', models.ManyToManyField(blank=True, to='main.fruit', verbose_name='Фрукт')),
                ('grain_id', models.ManyToManyField(blank=True, to='main.grain', verbose_name='Крупа')),
                ('meat_id', models.ManyToManyField(blank=True, to='main.meat', verbose_name='Мясо')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile', verbose_name='Профиль')),
                ('veg_id', models.ManyToManyField(blank=True, to='main.vegetable', verbose_name='Овощ')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]

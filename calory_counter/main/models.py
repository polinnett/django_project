from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from simple_history.models import HistoricalRecords


class Vegetable(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Овощ'
        verbose_name_plural = 'Овощи'
        ordering = ['name']


class Fruit(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрукт'
        verbose_name_plural = 'Фрукты'
        ordering = ['name']


class Meat(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мясо'
        verbose_name_plural = 'Мясо'
        ordering = ['name']


class Grain(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Крупа'
        verbose_name_plural = 'Крупы'
        ordering = ['name']


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    name = models.CharField(max_length=200, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    reg_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Record(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    veg_id = models.ManyToManyField(Vegetable, blank=True, verbose_name='Овощ')
    fruit_id = models.ManyToManyField(Fruit, blank=True, verbose_name='Фрукт')
    meat_id = models.ManyToManyField(Meat, blank=True, verbose_name='Мясо')
    grain_id = models.ManyToManyField(Grain, blank=True, verbose_name='Крупа')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

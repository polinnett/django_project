# Generated by Django 4.2.2 on 2023-06-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fruit',
            options={'ordering': ['name'], 'verbose_name': 'Фрукт', 'verbose_name_plural': 'Фрукты'},
        ),
        migrations.AlterModelOptions(
            name='grain',
            options={'ordering': ['name'], 'verbose_name': 'Крупа', 'verbose_name_plural': 'Крупы'},
        ),
        migrations.AlterModelOptions(
            name='meat',
            options={'ordering': ['name'], 'verbose_name': 'Мясо', 'verbose_name_plural': 'Мясо'},
        ),
        migrations.AlterModelOptions(
            name='vegetable',
            options={'ordering': ['name'], 'verbose_name': 'Овощ', 'verbose_name_plural': 'Овощи'},
        ),
        migrations.AlterField(
            model_name='fruit',
            name='carbohydrates',
            field=models.FloatField(verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='fats',
            field=models.FloatField(verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='proteins',
            field=models.FloatField(verbose_name='Белки'),
        ),
        migrations.AlterField(
            model_name='grain',
            name='carbohydrates',
            field=models.FloatField(verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='grain',
            name='fats',
            field=models.FloatField(verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='grain',
            name='proteins',
            field=models.FloatField(verbose_name='Белки'),
        ),
        migrations.AlterField(
            model_name='meat',
            name='carbohydrates',
            field=models.FloatField(verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='meat',
            name='fats',
            field=models.FloatField(verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='meat',
            name='proteins',
            field=models.FloatField(verbose_name='Белки'),
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='carbohydrates',
            field=models.FloatField(verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='fats',
            field=models.FloatField(verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='proteins',
            field=models.FloatField(verbose_name='Белки'),
        ),
    ]

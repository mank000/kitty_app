# Generated by Django 5.1.1 on 2024-10-03 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_cat_color_alter_breed_name_alter_cat_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(verbose_name='Возвраст(в месяцах)'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.breed', verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(max_length=128, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.CharField(blank=True, max_length=256, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
    ]

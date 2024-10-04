from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from kittyapi import const

User = get_user_model()


class Cat(models.Model):
    """Модель кота."""
    name = models.CharField('Имя',
                            max_length=const.MAX_NAME_LEN,
                            blank=False)
    description = models.CharField('Описание',
                                   max_length=const.MAX_DESC_LEN,
                                   blank=True)
    color = models.CharField('Цвет',
                             max_length=const.MAX_NAME_LEN,
                             blank=True)
    age = models.IntegerField('Возвраст(в месяцах)',
                              blank=False)
    breed = models.ForeignKey('cats.Breed',
                              verbose_name='Порода',
                              on_delete=models.CASCADE,
                              blank=False,
                              related_name='cats')
    owner = models.ForeignKey(User,
                              related_name='cats',
                              verbose_name='Владелец',
                              on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Breed(models.Model):
    """Модель породы"""
    name = models.CharField('Название породы',
                            max_length=const.MAX_NAME_LEN,
                            unique=True
                            )

    def __str__(self) -> str:
        return self.name


class CatRating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings')
    cat = models.ForeignKey(
        Cat,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.rating

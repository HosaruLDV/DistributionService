from datetime import date

from django.db import models

class Blog(models.Model):
    header = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.CharField(max_length=1500, verbose_name='Содержание')
    image = models.FileField(verbose_name='Изображение', upload_to='blog/')
    views = models.IntegerField(verbose_name='Кол-во просмотров')
    published_data = models.DateField(default=date.today(), verbose_name='Дата')

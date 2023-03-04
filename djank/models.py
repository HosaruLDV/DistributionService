from django.db import models
from datetime import date


# Create your models here.

class Client(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    middle_name = models.CharField(max_length=250, verbose_name='Отчество')
    email = models.CharField(max_length=250, verbose_name='Почта')
    comment = models.CharField(max_length=250, verbose_name='Комментарий')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    theme = models.CharField(max_length=250, verbose_name='тема')
    text = models.CharField(max_length=250, verbose_name='текст')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.theme}'


class DistributionList(models.Model):
    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'
    STATUS_COMPLETED = 'completed'
    STATUSES = (
        (STATUS_CREATED, 'создано'),
        (STATUS_LAUNCHED, 'запущено'),
        (STATUS_COMPLETED, 'завершено')
    )

    PERIOD_DAY = 'day'
    PERIOD_WEEK = 'week'
    PERIOD_MONTH = 'month'
    PERIODS = (
        (PERIOD_DAY, 'день'),
        (PERIOD_WEEK, 'неделя'),
        (PERIOD_MONTH, 'месяц')
    )
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    time = models.TimeField(null=True, verbose_name='Время рассылки')
    date = models.DateField(default=date.today(), verbose_name='Дата')
    periodicity = models.CharField(choices=PERIODS, default=PERIOD_DAY, max_length=10, verbose_name='Период')
    status = models.CharField(choices=STATUSES, default=STATUS_CREATED, max_length=10, verbose_name='Статус')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
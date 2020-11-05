from django.contrib.auth.models import User
from django.db import models


class Argue(models.Model):
    title = models.CharField('Заголовок', max_length=140)
    text = models.TextField('Описание')
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_argues', verbose_name='Вызывающий')
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='argues', verbose_name='Вызываемый')
    opened = models.DateTimeField('Спор открыт', default=None, null=True)
    closed = models.DateTimeField('Спор разрешен', default=None, null=True)
    active = models.BooleanField('Активно', default=True)

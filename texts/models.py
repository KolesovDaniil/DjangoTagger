from django.contrib.auth.models import User
from django.db import models


class Text(models.Model):

    def __str__(self):
        return self.text

    text = models.TextField(verbose_name='Текст')
    creation_dt = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    last_update_dt = models.DateTimeField(verbose_name='Дата последнего редактирования', null=True)
    tags = models.TextField(verbose_name='Тэги')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='texts')

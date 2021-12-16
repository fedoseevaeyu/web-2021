from django.db import models


class ProgramLanguage(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

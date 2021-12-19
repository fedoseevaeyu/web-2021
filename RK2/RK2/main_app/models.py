from django.db import models


class Supplier(models.Model):
    id_sup = models.AutoField('id_sup', primary_key=True)
    name = models.IntegerField(verbose_name='Имя')
    country = models.CharField(max_length=1, verbose_name='Страна')

    def __str__(self):
        return f'{self.number}{self.letter}'


class Detail(models.Model):
    id_det = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    material = models.IntegerField(verbose_name='Материал')
    id_class = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='id_sup', verbose_name='Производитель')

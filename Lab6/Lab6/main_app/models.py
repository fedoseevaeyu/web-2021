# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProgLanguage(models.Model):
    id_language = models.AutoField(db_column='ID_language', primary_key=True)  # Field name made lowercase.
    language_name = models.CharField(db_column='Language_name', max_length=100, blank=True, null=False)  # Field name made lowercase.
    descript = models.CharField(db_column='Descript', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    creation_year = models.IntegerField(db_column='Creation_year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Prog_language'


class App(models.Model):
    id_app = models.AutoField(db_column='ID_app', primary_key=True)  # Field name made lowercase.
    application_name = models.CharField(db_column='Application_name', max_length=100, blank=True, null=False)  # Field name made lowercase.
    developer = models.CharField(db_column='Developer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_language = models.ForeignKey('ProgLanguage', models.DO_NOTHING, db_column='ID_language', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'App'

from django.shortcuts import render

from .serializers import LangSerializer
from .models import *
from django.apps import apps
from rest_framework import viewsets


def index(request):
    models = apps.get_app_config('main_app').get_models()
    models_names = [model._meta.db_table for model in models]
    models_dict = {model_id: models_name for model_id, models_name in zip(range(len(models_names)), models_names)}
    params = {'models_dict': models_dict}
    print(params)
    return render(request, 'index.html', params)


def list(request, model_name):
    models = apps.get_app_config('main_app').get_models()
    model = ''
    for elem in models:
        if elem._meta.db_table == model_name:
            model = elem
    params = {  'model_name': model._meta.db_table, 
                'objects': model.objects.values()}
    return render(request, 'list.html', params)

class LangViewSet(viewsets.ModelViewSet):
    queryset = ProgLanguage.objects.all()
    serializer_class = LangSerializer

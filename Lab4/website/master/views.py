from django.http import HttpResponse
from django.shortcuts import render
from .models import ProgramLanguage
from django.http import HttpResponseRedirect


def master(request):
    languages = {'languages': ProgramLanguage.objects.order_by('id')}
    return render(request, 'list.html', languages)


def detail(request, lang_id):
    language = ProgramLanguage.objects.get(id=lang_id)
    return render(request, 'detail.html', {'language': language})

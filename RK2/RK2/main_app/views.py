from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from .models import *
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def report(request):
    details = Detail.objects.all()
    params = {'details': details, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return render(request, 'report.html', params)

def supplier_list(request):
    suppliers = Supplier.objects.all().values()
    params = {'entity': 'Supplier', 'objects': suppliers}
    return render(request, 'list.html', params)

def detail_list(request):
    details = Detail.objects.all().values()
    params = {'entity': 'Detail', 'objects': details}
    return render(request, 'list.html', params)

class SupplierCreate(CreateView):
    model = Supplier
    fields = ['name', 'country']
    success_url = '/supplier'
    template_name = 'supplier_form.html'

class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['name', 'country']
    pk_url_kwarg = 'id_sup'
    success_url = '/supplier'
    template_name = 'supplier_form.html'
    
class SupplierDelete(DeleteView):
    model = Supplier
    pk_url_kwarg = 'id_sup'
    success_url = '/sup'
    template_name = 'sup_delete_form.html'

class DetailCreate(CreateView):
    model = Detail
    fields = ['name', 'material']
    success_url = '/detail'
    template_name = 'detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(DetailCreate, self).get_context_data(**kwargs)
        context['form'].fields['id_sup'] = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label=None, label='Производитель')
        return context

class DetailUpdate(UpdateView):
    model = Detail
    fields = ['name', 'material']
    pk_url_kwarg = 'id_det'
    success_url = '/detail'
    template_name = 'detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(DetailUpdate, self).get_context_data(**kwargs)
        context['form'].fields['id_det'] = forms.ModelChoiceField(queryset=Supplier.objects.all(), empty_label=None, label='Производитель')
        return context

class DetailDelete(DeleteView):
    model = Detail
    pk_url_kwarg = 'id_det'
    success_url = '/detail'
    template_name = 'detail_delete_form.html'
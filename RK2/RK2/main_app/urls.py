from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('supplier', views.supplier_list),
    path('supplier/create', views.SupplierCreate.as_view()),
    path('supplier/<int:id_sup>/update', views.SupplierUpdate.as_view(), name='sup_update'),
    path('supplier/<int:id_sup>/delete', views.SupplierDelete.as_view(), name='sup_delete'),
    path('detail', views.detail_list),
    path('detail/create', views.DetailCreate.as_view()),
    path('detail/<int:id_det>/update', views.DetailUpdate.as_view(), name='det_update'),
    path('detail/<int:id_det>/delete', views.DetailDelete.as_view(), name='det_delete'),
    path('report', views.report)
]
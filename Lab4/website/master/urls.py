from django.urls import path
from . import views

urlpatterns = [
    path('', views.master, name='master'),
    path('<int:lang_id>/', views.detail, name='detail')
]

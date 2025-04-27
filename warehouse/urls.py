from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_show, name='warehouse_show'),
]

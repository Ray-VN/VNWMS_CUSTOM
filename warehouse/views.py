from django.shortcuts import render
from warehouse.models import Warehouse


def warehouse_show(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse_list.html', locals())
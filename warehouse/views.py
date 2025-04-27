from django.shortcuts import render


# Create your views here.
def warehouse_show(request):
    return render(request, 'warehouse_list.html', locals())
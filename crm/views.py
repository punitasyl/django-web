from django.shortcuts import render
from .models import Orders

def first_page(request):
    object_list = Orders.objects.all()
    return render(request, './index.html', {'object_list': object_list})

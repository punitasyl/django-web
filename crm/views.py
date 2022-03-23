from django.shortcuts import render

from .forms import OrderForm
from .models import Orders
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram

def first_page(request):
    slider_lists = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()

    form = OrderForm()

    dic_objects = {'slider_list': slider_lists,
                   'pc_1': pc_1,
                   'pc_2': pc_2,
                   'pc_3': pc_3,
                   'price_table': price_table,
                   'form': form
                   }

    return render(request, './index.html', dic_objects)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Orders(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', { 'name': name,})
    else:
        return render(request, './thanks.html')
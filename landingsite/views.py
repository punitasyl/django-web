from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = 5445
    text = 'Text from data'
    return render(request, './index.html', {
        'a': a,
        'text': text,
    })

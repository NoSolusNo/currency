from django.shortcuts import render
from django.http.response import HttpResponse
from currency.models import Rate, ContactUs


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World Pull Request for Homework4')


def rate_list(request):
    rates = Rate.objects.all()
    result = []
    # breakpoint()
    for rate in rates:
        result.append(f'<br>Валюта: {rate.type} Покупка: {rate.buy} Продажа: {rate.sale}')
    return HttpResponse(str(result))


def contact_list(request):
    contacts = ContactUs.objects.all()
    result = []
    # breakpoint()
    for contact in contacts:
        result.append(f'<br>Почта: {contact.email_from} Покупка: {contact.subject} Продажа: {contact.message}')
    return HttpResponse(str(result))

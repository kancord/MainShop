from django.shortcuts import render
from django.http import *
import warehouse.models as mdl
# Create your views here.
def catalog(request):
#    a = mdl.Category(name='Бытовая техника')
#    a.save()
#   b=mdl.Product(name='Пылесос №1',
#                               decsription='Модель №1',
#                               price=3500,
#                               category=mdl.Category.objects.get(name='Бытовая техника'))
#    b.save()
#    c = mdl.warehouse(product=mdl.Product.objects.get(name='Пылесос №1'),
#                                   count=4)
#    c.save()

    return HttpResponse("<h1> Hello world </h1>")
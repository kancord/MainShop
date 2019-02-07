from django.shortcuts import render
from django.http import *
import warehouse.models as mdl
from .models import Product,Warehouse,Category
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

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_products=Product.objects.all().count()  #количество товаров в базе
    stocks = Warehouse.objects.all()
    num_stocks = 0 #Количество товаров на складе всего
    for tmp in stocks:
        num_stocks += tmp.count


    return render(request,'index.html',
                  context={'num_products':num_products,'num_stocks':num_stocks})
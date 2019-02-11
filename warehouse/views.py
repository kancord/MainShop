from django.shortcuts import render
from django.http import *
from django.views import generic
from .models import Product,Warehouse,Category, Cart
# Create your views here.
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

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'Товары'
    #queryset = Product.objects.all()
    template_name = 'product_list.html'
    paginate_by = 10

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

class CartListView(generic.ListView):
    model = Cart
    template_name = 'cart_list.html'
    paginate_by = 10

    def get_queryset(self):
       if self.request.user.is_active:
           return Cart.objects.filter(customer=self.request.user).order_by('date')
       return Cart.objects.none()

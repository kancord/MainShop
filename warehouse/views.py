from django.shortcuts import render
from django.http import *
from django.views import generic
from .models import Product,Warehouse,Category, Cart
from .forms import SearchEngineForm
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
    #отображение товаров
    model = Product
    context_object_name = 'Товары'
    template_name = 'product_list.html'
    paginate_by = 25

    def get_queryset(self):
        filter_id = self.request.GET.get('filter_cat','')
        if (filter_id == ''):
            new_context=Product.objects.all()
        else:
            new_context = Product.objects.filter(category_id=filter_id)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['filter'] = SearchEngineForm(self.request.GET)
        return context



class ProductDetailView(generic.DetailView):
    #детально обображение товаров
    model = Product
    template_name = 'product_detail.html'

class CartListView(generic.ListView):
    #отображение купленных товаров
    model = Cart
    template_name = 'cart_list.html'
    paginate_by = 10


    def get_queryset(self):
       if self.request.user.is_active:
           return Cart.objects.filter(customer=self.request.user).order_by('date')
       return Cart.objects.none()

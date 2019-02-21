"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import warehouse.views
from django.views.generic import RedirectView
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from warehouse.serializers import *

router = routers.DefaultRouter()
router.register(r'products_api', warehouse.views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^cart/$',warehouse.views.CartListView.as_view(), name='cart'),
    re_path(r'^products/$',warehouse.views.ProductListView.as_view(), name='products'),
    re_path(r'^products/(?P<pk>\d+)$', warehouse.views.ProductDetailView.as_view(), name='product-detail'),
    re_path(r'^products/(?P<pk>\d+)/order$', warehouse.views.confurmOrder, name='product-order'),
    re_path(r'^index/$', warehouse.views.index, name='index'),
    #re_path(r'^$', RedirectView.as_view(url=' index/', permanent=True)), #пустая адресная строка
    #re_path(r'.*', RedirectView.as_view(url='index/', permanent=True)), #любая строка
    path('', warehouse.views.index),
]

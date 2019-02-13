from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    #Категория товара
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        #Порядок
        ordering = ['name']

class Product(models.Model):
    #Товар
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
      '''Служит для формирования ссылки'''
      from django.urls import reverse
      return reverse('product-detail', args=[str(self.id)])

    class Meta:
        # Порядок
        ordering = ['price']

class Warehouse(models.Model):
    # Доступность на складе
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    count = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.product.name, self.count)


    class Meta:
        # Порядок
        ordering = ['product']

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    count = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return '{0} {1} шт  {2}'.format(self.product.name, self.count, self.date)

    class Meta:
        # Порядок
        ordering = ['date']

    def get_absolute_url(self):
      '''Служит для формирования ссылки'''
      from django.urls import reverse
      return reverse('product-detail', args=[str(self.id)])

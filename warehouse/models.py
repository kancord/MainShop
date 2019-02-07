from django.db import models

class Category(models.Model):
    #Категория товара
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    #Товар
    name = models.CharField(max_length=50, unique=True)
    decsription = models.TextField(max_length = 500)
    price = models.IntegerField()
    category =models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    # Доступность на складе
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    count = models.IntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.product.name, self.count)
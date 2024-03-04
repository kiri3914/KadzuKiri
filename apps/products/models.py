from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(verbose_name = 'Описание категории')

    def __str__(self):
        return f'Категория:{self.title}'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена товара')
    is_available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    base_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Название продукта: {self.name}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    

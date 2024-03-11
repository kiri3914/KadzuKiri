from typing import Iterable
from django.db import models
from apps.authorization.models import User
from apps.products.models import Product


# Создаем клиента
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    image = models.ImageField(upload_to='clients/', blank=True, null=True)
    
    def __str__(self):
        return self.user
    
    
# Адрес клиента
class Adress(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='customer_adress')
    city = models.CharField(max_length=40, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    home = models.CharField(max_length=10, verbose_name='Номер дома')
    
    def __str__(self):
        return f'Город: {self.city}\n'\
               f'Улица: {self.street}\n'\
               f'Дом: {self.home}' 
    
    
# Избранное клиента
class Favorites(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_favorites')

    def __str__(self):
        return f'{self.customer} - {self.product}'
    
    
# Корзина
class Cart(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cart_client')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    count_product = models.IntegerField(default=0, verbose_name='Количество')
    cost_product = models.IntegerField(default=0, verbose_name='Стоимость')
    
    def __str__(self):
        return f'{self.customer} - {self.created_at}'
    
    
# Товар в корзине
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
    count = models.IntegerField(verbose_name='Количество товаров')
    total_price = models.FloatField(verbose_name='Стоимость', default=0.0, blank=True, null=True)
    added_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    def __str__(self):
        return f'{self.cart} - {self.product}'
    
    def save(self,  *args, **kwargs) -> None:
        self.total_price = self.product.price * self.count
        super().save(*args, **kwargs)


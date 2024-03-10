from django.db import models
from apps.customers.models import Adress, Cart


class Delivery(models.Model):
    DELIVERY_STATUS = (
        ('new', 'Новый'),
        ('inprocess', 'В процессе'),
        ('onaway', 'В пути'),
        ('delivered', 'Доставлено'),
        ('cancel', 'Отменено'),
    )

    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, related_name='deliver_address')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='deliver_cart')
    delivery_status = models.CharField(choices=DELIVERY_STATUS, max_length=20, default='new')
    order_number = models.IntegerField()
    delivery_date = models.DateTimeField()

    def __str__(self):
        return self.adress

    def gen_order_number(self):
        from random import randrange
        return randrange(1000,9999)

    def save(self, *args, **kwargs):
        if self.delivery_status == 'new':
            self.order_number = self.gen_order_number()
        super().save(*args, **kwargs)
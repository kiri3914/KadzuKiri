from django.db import models
from apps.customers.models import Adress, Cart


class StatusDeliver(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Delivery(models.Model):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_status = models.ForeignKey(StatusDeliver, on_delete=models.CASCADE)
    number = models.IntegerField(max_length=12)
    delivery_date = models.DateTimeField()
    tracking_number = models.IntegerField()
    delivery_cost = models.IntegerField()

    def __str__(self):
        return self.adress

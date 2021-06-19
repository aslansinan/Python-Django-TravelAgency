from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm
from product.models import Product


class ReservationCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)


class ReservationCartForm(ModelForm):
    class Meta:
        model= ReservationCart
        fields = ['quantity']
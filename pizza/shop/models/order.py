from django.db import models

# Create your models here.
#from decimal import Decimal
from .pizza import Pizza

class Order(models.Model):

    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, default='', blank=True, null=True)
    phone = models.CharField(max_length=150, default='', blank=True, null=True)
    address = models.CharField(max_length=150, default='', blank=True, null=True)


    def __str__(self):
        return '%s' % (pizza.name)

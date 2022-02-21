from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateField(auto_now=True)
    ored_name = models.CharField(max_length=200)
    oder_phone = models.CharField(max_length=200)
    
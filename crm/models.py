from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateField(auto_now=True)
    order_name = models.CharField(max_length=200,verbose_name='ismi')
    order_phone = models.CharField(max_length=200,verbose_name='telefon')
    
    
    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = 'zakaz'
        verbose_name_plural = 'zakazlar'
        
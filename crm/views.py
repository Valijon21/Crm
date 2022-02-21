from ssl import HAS_TLSv1_2
from django.shortcuts import render
from .models import Order
# Create your views here.
def firs_page(request):
    
    object_list = Order.objects.all() # mdul ichida hamma queriset malumotlarni ol diyapmiz
    context = {'object_list':object_list}
    return  render(request,'./index.html',context)


def thanks(request):
    name = request.GET['name']
    phone = request.GET['phone']
    
    return  render(request,'./thank.html',{'name':name,
                                           'phone':phone})
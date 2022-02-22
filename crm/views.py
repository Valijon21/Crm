from ssl import HAS_TLSv1_2
from django.shortcuts import render
from .models import Order
from .forms import Orderform
# Create your views here.
def firs_page(request):
    
    object_list = Order.objects.all() # mdul ichida hamma queriset malumotlarni ol diyapmiz
    form = Orderform() # form uzgaruvchiga Orderform classni yuklaymiz va renderga beramiz
    context = {'object_list':object_list,'form':form}
    return  render(request,'./index.html',context)


def thanks(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element_sav = Order(order_name = name, order_phone = phone)
    element_sav.save()
    return  render(request,'./thank.html',{'name':name,
                                           'phone':phone})
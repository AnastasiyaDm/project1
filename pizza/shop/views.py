from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
#from .forms import RegForm
from account.forms import CustomerRegForm as RegForm
from .lib.shop_class import Shop
from .models.pizza import Pizza
from .models.order import Order
from .forms import OrderForm
import logging
# Create your views here.


logger = logging.getLogger(__name__)


def order(request,pizza_id):
    pizza = Pizza.objects.get(pk=pizza_id)
    orders = Order.objects.all()
    o=Order()
    o.pizza=pizza
    o.save()
    messages.warning(request, 'Success!!!')
    return render(request,'shop/order_list.html',{'orders': orders})

def detail(request,name):
    pizza = Pizza.objects.get(name_slug=name)
    order=Order()
    order.pizza=pizza
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            messages.warning(request, 'Order has been saved.')
            form.save()
            form = OrderForm(instance=order)
        else:
            messages.warning(request, 'Error!!')
    return render(request,'shop/detail.html',{'pizza': pizza,'form':form})


def home(request):
    logger.debug('Something went wrong!')
    form = RegForm()
    shop = Shop()
    pizzas = Pizza.objects.all()
    return render(request,'shop/home.html', {'shop': shop, 'form': form,'pizzas': pizzas})

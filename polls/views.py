from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Product, OrderItem, Order

class IndexView(generic.ListView):
    model = Product
    template_name = 'polls/index.html'
    context_object_name = 'product_list'


class DetailView(generic.DetailView):
    model = Product
    template_name = 'polls/product.html'

class OrderView(generic.ListView):
    model = OrderItem
    template_name = 'polls/shopping_cart.html'
    context_object_name = 'order_list'

    def cart_total(self):
        return sum(model.price for order in order_list)

def getOrderItems(request):
    items = OrderItem.objects.all()
    total = 0
    for item in items:
        total+=item.item.price*item.quantity

    return render(request,'polls/shopping_cart.html',{'total':total, 'order_list':items})

def deleteOrder(request, pk):
    order = OrderItem.objects.filter(pk=pk)
    if order.exists():
        order.delete()
    
    return redirect('polls:order')
    

def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(item=item)
    order_qs = Order.objects.filter(ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create()
        order.items.add(order_item)
    return redirect("polls:detail",pk)
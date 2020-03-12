from django.contrib import admin
from .models import Product, OrderItem, Order
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','image','country','color','flavor')



admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)

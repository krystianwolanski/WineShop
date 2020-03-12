from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add-to-cart'),
    path('order/',views.getOrderItems, name='order'),
    path('order/delete/<int:pk>/',views.deleteOrder, name='deleteOrder')
]
from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):

    ARG = 'Argentyna'
    AUS = 'Australia'
    AUT = 'Austria'
    FRA = "Francja"
    ITA = "Włochy"
    POR = 'Portugalia'
    GRU = 'Gruzja'
    MOL = 'Mołdawia'
    SPA = 'Hiszpania'
    NZ = 'Nowa Zelandia'
    USA = 'USA'
    GER = 'Niemcy'
    COUNTRY_CHOICES = (
        (ARG,'Argentyna'),
        (AUS,'Australia'),
        (AUT,'Austria'),
        (FRA,'Francja'),
        (ITA,'Włochy'),
        (POR,'Portugalia'),
        (GRU,'Gruzja'),
        (MOL,'Mołdawia'),
        (SPA,'Hiszpania'),
        (NZ,'Nowa Zelandia'),
        (USA, 'USA'),
        (GER, 'Niemcy')
        
    )

    BIALE = 'Białe'
    CZERWONE = 'Czerwone'
    ROZOWE = 'Różowe'
    COLOR_CHOICES = (
        (BIALE,'Białe'),
        (CZERWONE,'Czerwone'),
        (ROZOWE,'Różowe')
    )

    WYTRAWNE = 'Wytrawne'
    POLWYTRAWNE = 'Półwytrawne'
    SLODKIE = 'Słodkie'
    POLSLODKIE = 'Półsłodkie'
    FLAVOR_CHOICES = (
        (WYTRAWNE,'Wytrawne'),
        (POLWYTRAWNE,'Półwytrawne'),
        (SLODKIE,'Słodkie'),
        (POLSLODKIE,'Półsłodkie')
    )

    name = models.CharField(max_length=200)
    description = models.CharField(max_length = 500, null=True, blank= True)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    image = models.ImageField(upload_to='wines/')
    country = models.CharField(max_length = 30, choices = COUNTRY_CHOICES)
    color = models.CharField(max_length = 20, choices = COLOR_CHOICES)
    flavor = models.CharField(max_length = 20, choices = FLAVOR_CHOICES)

    def __str__(self):
        return self.name
    def get_add_to_cart_url(self):
        return reverse("polls:add-to-cart",kwargs={
            'pk':self.pk
        })
    
class OrderItem(models.Model):
    #ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
    def multiplication(self):
        return self.quantity*self.item.price
    

class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    date_added = models.DateTimeField(auto_now = True)
    date_added.editable = True
    ordered_date = models.DateTimeField(blank = True, null = True)
    ordered = models.BooleanField(default = False)






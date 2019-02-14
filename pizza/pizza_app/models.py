from django.db import models


class Pizza(models.Model):
    PIZZA_SIZE = (
        ('R', 'Regular'),
        ('B', 'Big'),
        ('S', 'Small'),
    )
    name                         = models.CharField(max_length=100)
    size                         = models.CharField(max_length=1, choices=PIZZA_SIZE)
    previous_regular_pizza_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)    
    current_regular_pizza_price  = models.DecimalField(max_digits=6, decimal_places=2)
    current_big_pizza_price      = models.DecimalField(max_digits=6, decimal_places=2)
    current_small_pizza_price    = models.DecimalField(max_digits=6, decimal_places=2)
    image                        = models.FileField()
    
    def __str__(self):
        return self.name


class PizzaChoice(models.Model):        
    name      = models.CharField(max_length=100)
    size      = models.CharField(max_length=20)
    quantity  = models.IntegerField()
    equation  = models.CharField(max_length=100)
    price     = models.DecimalField(max_digits=6, decimal_places=2)
    client_ip = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
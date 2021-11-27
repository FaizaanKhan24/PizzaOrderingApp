from django.db import models

# Create your models here.

class RegularPizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    small_pizza_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    large_pizza_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    toppings_available = models.IntegerField()

    def returnPrice(self,isLarge):
        if isLarge:
            return large_pizza_price
        else:
            return small_pizza_price

    def __str__(self):
        return f"Regular Pizza : {self.pizza_name}, Small : {self.small_pizza_price}, Large: {self.large_pizza_price}, Toppings Available: {self.toppings_available}"

class SicilianPizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    small_pizza_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    large_pizza_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    toppings_available = models.IntegerField()

    def __str__(self):
        return f"Sicilian Pizza : {self.pizza_name}, Small : {self.small_pizza_price}, Large: {self.large_pizza_price}, Toppings Available: {self.toppings_available}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Subs(models.Model):
    sub_name = models.CharField(max_length=64)
    small_sub_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    large_sub_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.sub_name} Small : {self.small_sub_price}, Large : {self.large_sub_price}"

class Pasta(models.Model):
    pasta_name = models.CharField(max_length=64)
    pasta_price = models.DecimalField(max_digits=4, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.pasta_name} Price : {self.pasta_price}"

class Salads(models.Model):
    salad_name = models.CharField(max_length=64)
    salad_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.salad_name} Price : {self.salad_price}"

class DinnerPlatters(models.Model):
    platter_name = models.CharField(max_length=64)
    small_platter_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    large_platter_price = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.platter_name} Small : {self.small_platter_price}, Large : {self.large_platter_price}"

class OrdersList(models.Model):
    item_name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    username = models.CharField(max_length=64)
    extras = models.CharField(max_length=128, null=True, blank=True)
    isOrderPlaced = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ordered {self.item_name} - {self.size}. \n Extras : {self.extras}  Cost : $ {self.price} Ordered : {self.isOrderPlaced}"
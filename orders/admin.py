from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(OrdersList)
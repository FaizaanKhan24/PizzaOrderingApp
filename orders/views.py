from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.error(request, f"{ form.error }")
        
        context = {'form':form}
        return render(request,'RegistrationPage.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,"LoginPage.html",{"message": "Wrong credentials bro"})

        return render(request,'LoginPage.html')

def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}
    context.update({"RegularPizza" : RegularPizza.objects.all()})
    context.update({"SicilianPizza" : SicilianPizza.objects.all()})
    context.update({"Toppings" : Toppings.objects.all()})
    context.update({"Subs" : Subs.objects.all()})
    context.update({"Pasta" : Pasta.objects.all()})
    context.update({"Salads" : Salads.objects.all()})
    context.update({"DinnerPlatter" : DinnerPlatters.objects.all()})
    return render(request,'MenuPage.html',context)

@login_required(login_url='login')
def Add_to_cart(request, item_type, item_size, item_id,):
    username = request.user.username
    item_list = item_type.split("&&")
    item_type = item_list[0]
    extra = (",".join(item_list[1:]))

    if item_type.lower() == "rpizza":
        pizza = RegularPizza.objects.get(id=item_id)
        name = pizza.pizza_name
        price = pizza.large_pizza_price if item_size.lower() == "large" else pizza.small_pizza_price                

        order = OrdersList(item_name=name,size=item_size,price=price,username=username,extras=extra)
        order.save()

        messages.add_message(request, messages.INFO, f"{name} Regular pizza Added")

    elif item_type.lower() == "spizza":
        pizza = SicilianPizza.objects.get(id=item_id)
        name = pizza.pizza_name
        price = pizza.large_pizza_price if item_size.lower() == "large" else pizza.small_pizza_price  

        order = OrdersList(item_name=name,size=item_size,price=price,username=username,extras=extra)    
        order.save() 

        messages.add_message(request, messages.INFO, f"{name} Sicilian pizza Added") 

    elif item_type.lower() == "sub":
        sub = Subs.objects.get(id=item_id)
        name = sub.sub_name
        price = sub.large_sub_price if item_size.lower() == "large" else sub.small_sub_price

        order = OrdersList(item_name=name, size=item_size, price=price, username=username)        
        order.save()

        messages.add_message(request, messages.INFO, f"{name} Sub Added") 

    elif item_type.lower() == "pasta":
        pasta = Pasta.objects.get(id=item_id)
        name = pasta.pasta_name
        price = pasta.pasta_price

        order = OrdersList(item_name=name, size="Regular", price=price, username=username)
        order.save()

        messages.add_message(request, messages.INFO, f"{name} Pasta Added") 

    elif item_type.lower() == "salad":
        salad = Salads.objects.get(id=item_id)
        name = salad.salad_name
        price = salad.salad_price

        order = OrdersList(item_name=name, size="Regular", price=price, username=username)
        order.save()

        messages.add_message(request, messages.INFO, f"{name} Salad Added") 

    elif item_type.lower() == "platter":
        dinnerPlatter = DinnerPlatters.objects.get(id=item_id)
        name = dinnerPlatter.platter_name
        price = dinnerPlatter.large_platter_price if item_size.lower() == "large" else dinnerPlatter.small_platter_price

        order = OrdersList(item_name=name, size=item_size, price=price, username=username)
        order.save()

        messages.add_message(request, messages.INFO, f"{name} Dinner Platter Added") 

    return HttpResponseRedirect(reverse('home'))

@login_required(login_url="login")
def Cart(request):
    username = request.user.username
    cart_items = OrdersList.objects.filter(username=username, isOrderPlaced=False)
    cart_total = 0
    for item in cart_items:
        cart_total = cart_total + item.price
    context = {}
    context.update({"cart_items":cart_items})
    context.update({"cart_total":cart_total})

    return render(request,"UserCartPage.html",context)

@login_required(login_url="login")
def PlaceOrder(request):
    username = request.user.username
    items_user_added = OrdersList.objects.filter(username=username)
    items_user_added.update(isOrderPlaced=True)

    messages.success(request, "Order Placed")

    return HttpResponseRedirect(reverse('home')) 

@login_required(login_url="login")
def RemoveItem(request, item_id):
    username = request.user.username
    items_user_added = OrdersList.objects.filter(username=username)
    item_name = items_user_added.get(id=item_id).item_name
    items_user_added.filter(id=item_id).delete()  

    messages.error(request, f"{item_name} deleted")  

    return HttpResponseRedirect(reverse('cart'))

@login_required(login_url="login")
def Orders(request):
    orders = OrdersList.objects.filter(isOrderPlaced = True)
    context = {}
    context.update({ "orders": orders })
    
    return render(request, "OrdersPage.html", context)
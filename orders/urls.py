from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.Register, name="register"),
    path("login",views.LoginPage,name="login"),
    path("logout",views.Logout,name="logout"),
    path("add/<str:item_type>/<str:item_size>/<int:item_id>",views.Add_to_cart,name="addToCart"),
    path("cart",views.Cart,name="cart"),
    path("place_order",views.PlaceOrder,name="place_order"),
    path("remove/<int:item_id>", views.RemoveItem,name="remove_item"),
    path("orders",views.Orders, name="orders")
]

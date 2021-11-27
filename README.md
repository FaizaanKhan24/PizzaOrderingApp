# Pizza Ordering Web Application

Web Programming with Python and JavaScript

Pinnochi's Pizza ordering web application using Django and JavaScript.

[Demo Link](https://www.youtube.com/watch?v=fz3sSc_QcrI)

This web application is build with the help of Python's Web framework Django and some help from JavaScript.

A small idea is given below for the functions of the app through Django and JavaScript.

<h4>Menu and Adding item:</h4>
A model for all the dishes in the menu card were created with the help of model classes for each and every category of dishes available in the restaurant. The dishes were added to the menu with the help of the admin module available for super users.

<h4>Registration, Login and Logout:</h4>
Django's authentication library was used for registering a new user and giving them access to the website.

<h4>Shopping Cart:</h4>
A model was created in models.py to add the items that the user selects. They are added to the cart. This items could be viewed in the cart page for each and every user.

<h4>Placing a Order:</h4>
There is an option to place an order of all the items in the cart and also the total amount of the cart is also displayed.

<h4>Viewing Order:</h4>
The admin has a view option to view the orders that the restaurant has received. All the orders made by all users including the size of the order, username and also the toppings user has selected. This option is only available for the admin. Normal users cannot view the orders.

<h4>Personal Touch:</h4>
In the cart section, the user has an option to remove the item from his cart if they do not require it. This was achieved with the help of JavaScript.

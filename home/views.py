from django.shortcuts import render
from django.conf import settings
from .models import Restaurant
import datetime

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def home(request):
    restaurant=
    Restaurant.objects.first()
    context={
        "restaurant_name":
        restaurant_name if restaurant else "Our Restaurant",

        context ={
            "restaurant_name":
        restaurant_name,    
        }
        #Hardcoded menu items
        "menu_items":[
            {"name":"Margherita Pizza","price":"Rs.250"},
            {"name":"Veg Burger","price":"Rs.150"},
            {"name":"Pasta Alfredo","price":"Rs.300"}
            {"name":"French Fries","price":"Rs.100"},
        ],
        "restaurant_logo":"/static/images/logo.png" #adding logo path
    }
    return render(request, "home/index.html", context)

    def contact(request):
        restaurant =
        Restaurant.objets.first()
          restaurant_name = restaurant.name
       if restaurant else "Our Restaurant"

       context = {
              "restaurant_name":
          restaurant_name, 
              "restaurant_phone":
          getattr(settings,"RESTAURANT_PHONE","+912198908870"),
             "restaurant_email":
         getattr("settings.RESTAURANT_EMAIL","support@example.com")
              "restaurant_address":
          getattr("settings.Restaurant_ADDRESS","123,Default Street,India"),
               "now":datetime.datetime.now(), #Adding new
                  
       } 

       def reservtions(request):
        restaurant =
        Restaurant.objects.first()
        context = {
            "restaurant_name":
       restaurant.name if restaurant else "Our Restaurant"     
        }  
    return render(request, "home/index.html", context)
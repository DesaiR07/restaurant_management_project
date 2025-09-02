from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def home(request):
    restaurant=
    Restaurant.objects.first()
    context={
        "restaurant_name":
        restaurant_name if restaurant else "Our Restaurant",
        #Hardcoded menu items
        "menu_items":[
            {"name":"Margherita Pizza","price":"Rs.250"},
            {"name":"Veg Burger","price":"Rs.150"},
            {"name":"Pasta Alfredo","price":"Rs.300"}
            {"name":"French Fries","price":"Rs.100"},
        ]
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
          settings.RESTAURANT_PHONE,
             "restaurant_email":
          settings.RESTAURANT_EMAIL,
              "restaurant_address":
           settings.Restaurant_ADDRESS,
                  
       }   
    return render(request, "home/contact.html", context)
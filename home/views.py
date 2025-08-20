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
        restaurant_name if restaurant else "Our Restaurant"
    }
    return render(request, "home/index.html", context)
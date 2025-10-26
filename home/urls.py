from django.urls import path
from .import views
from .views import MenuCategoryListView

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('reservations/',views.reservations,name='reservations')#new route]
    path('categories/', MenuCategoryListView.as_view(), name='menu-category-list')
]
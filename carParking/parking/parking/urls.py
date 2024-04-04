"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from parkingapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('list_booking/', views.booking_list, name='booking_list'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('add_fleet/', views.add_fleet, name='add_fleet'),
    path('list_fleet/', views.fleet_list, name='flight_list'),
    path('add_inventory/', views.add_inventory, name='add_inventory'),
    path('list_inventory/', views.inventory_list, name='inventory_list'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('list_vehicle/', views.vehicle_list, name='vehicle_list'),
    path('search/', views.search_vehicle_customer, name='search_vehicle_customer'),
    path('book/<int:vehicle_id>/', views.book_vehicle_customer, name='book_vehicle_customer'),
    path('vehicle_history/', views.vehicle_list_history, name='vehicle_history'),
    path('booking_history/', views.booking_list_history, name='booking_history'),
    path('fleet_history/', views.fleet_list_history, name='fleet_history'),
    path('inventory_history/', views.inventory_list_history, name='inventory_history'),
    path('delete/<str:model_name>/<int:id>/', views.delete_items, name='delete_item'),
    path('accounts/', include('registration.backends.default.urls')),

]

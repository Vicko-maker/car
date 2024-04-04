from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.apps import apps
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
import csv
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home page here

def home(request):
    title = "CAR BOOKING SYSTEM"
    context = {
        "title": title,
    }

    return render(request, "home.html", context)

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash password
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'])
            login(request, new_user)
            return redirect('home')  # Redirect to a desired page

    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })


@login_required#add aircraft here
def add_vehicle(request):
    form = VehicleCreate(request.POST or None)
    context = {
        "form": form,
        "title": "Add Aircraft",
    }
    return render(request, "add_vehicle.html", context)


@login_required
def vehicle_list(request):
    vehicle = Vehicle.objects.all()
    context = {
        "vehicle": vehicle,
    }

    return render(request, 'vehicle_list.html', context)

@login_required
def vehicle_list_history(request):
    vehicle = Vehicle.objects.all()
    form = VehicleSearchForm(request.POST or None)
    context = {
        "vehicle": vehicle,
        "form": form
    }
    if request.method == 'POST':
        queryset = Vehicle.objects.filter(model__icontains=form['model'].value(),
                                                 make__icontains=form['make'].value(),

                                                 )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="list of vehicle.csv"'
            writer = csv.writer(response)
            writer.writerow(['MODEL', 'MAKE'])
            instance = queryset
            for vehicle in instance:
                writer.writerow([vehicle.model, vehicle.make])
                return response

        context = {
            'form': form,
            'queryset': queryset
        }
    return render(request, 'vehicle_list_history.html', context)


@login_required
def add_booking(request):
    form = BookingCreate(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/list_booking')
    context = {
        "form": form,
        "title": "Add Booking",
    }
    return render(request, "add_booking.html", context)

@login_required
def booking_list(request):
    booking = Booking.objects.all()
    context = {
        "booking": booking,
    }
    return render(request, 'booking_list.html', context)

def booking_list_history(request):
    booking = Booking.objects.all()
    form = BookingSearchForm(request.POST or None)
    context = {
        "form": form,
        "booking": booking
    }
    if request.method == 'POST':
        queryset = Booking.objects.filter(start_date__icontains=form['start_date'].value(),
                                          end_date__icontains=form['end_date'].value(),
                                         )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="list of booking.csv"'
            writer = csv.writer(response)
            writer.writerow(['START DATE', 'END DATE'])
            instance = queryset
            for booking in instance:
                writer.writerow([booking.start_date, booking.end_date])
                return response

        context = {
            'form': form,
            'queryset': queryset
        }
    return render(request, 'booking_list_history.html', context)

@login_required
def add_fleet(request):
    form = FleetCreate(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/fleet_list')
    context = {
        "form": form,
        "title": "Add Fleet",
    }
    return render(request, "add_fleet.html", context)

@login_required
def fleet_list(request):
    fleet = Fleet.objects.all()
    context = {
        "fleet": fleet,
    }
    return render(request, 'fleet_list.html', context)

@login_required
def fleet_list_history(request):
    fleet = Fleet.objects.all()
    form = FleetSearchForm(request.POST or None)
    context = {
        "form": form,
        "fleet": fleet
    }
    if request.method == 'POST':
        queryset = Fleet.objects.filter(name__icontains=form['name'].value()
                                         )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="list of fleets.csv"'
            writer = csv.writer(response)
            writer.writerow(['NAME', 'VEHICLES'])
            instance = queryset
            for fleet in instance:
                writer.writerow([fleet.name, fleet.vehicles])
                return response

        context = {
            'form': form,
            'queryset': queryset
        }

    return render(request, 'fleet_list_history.html', context)

@login_required
def add_inventory(request):
    form = InventoryCreate(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/list_inventory')
    context = {
        "form": form,
        "title": "Add To Inventory",
    }
    return render(request, "add_inventory.html", context)

@login_required
def inventory_list(request):
    inventory = Inventory.objects.all()
    context = {
        "inventory": inventory,
    }
    return render(request, 'inventory_list.html', context)

@login_required
def inventory_list_history(request):
    inventory = Inventory.objects.all()
    form = InventorySearchForm(request.POST or None)
    context = {
        "form": form,
        "inventory": inventory
    }
    if request.method == 'POST':
        queryset = Inventory.objects.filter(vehicle__icontains=form['name'].value()

                                         )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="list of inventory.csv"'
            writer = csv.writer(response)
            writer.writerow(['VEHICLE', 'QUANTITY'])
            instance = queryset
            for inventory in instance:
                writer.writerow([inventory.vehicle, inventory.quantity])
                return response

        context = {
            'form': form,
            'queryset': queryset
        }

    return render(request, 'inventory_list_history.html', context)


def search_vehicle_customer(request):
    if request.method == 'POST':
        form = SearchFormCustomer(request.POST)
        if form.is_valid():
            vehicles = Vehicle.objects.filter(
                make=form.cleaned_data['make'],
                model=form.cleaned_data['model'],
                year=form.cleaned_data['year'],
                is_available=True
            )
            return render(request, 'search_results.html', {'vehicles': vehicles})
    else:
        form = SearchFormCustomer()
    return render(request, 'search_vehicle.html', {'form': form})

def book_vehicle_customer(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method == 'POST':
        form = BookingFormCustomer(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.vehicle = vehicle
            booking.customer = request.user.customer
            booking.save()
            # Handle booking logic
            return render(request, 'booking_confirmation.html', {'booking': booking})
    else:
        form = BookingFormCustomer()
    return render(request, 'book_vehicle.html', {'form': form, 'vehicle': vehicle})


def delete_items(request, model_name, id):
    # Map the string model_name to actual model classes
    model_map = {
        'vehicle': Vehicle,
        'booking': Booking,
        'fleet': Fleet,
        'inventory': Inventory,
    }

    # Get the model class from the map
    model = model_map.get(model_name.lower())

    if not model:
        raise Http404(f"No model found for {model_name}")

    # Get the specific object and delete it
    obj = get_object_or_404(model, id=id)
    obj.delete()

    messages.success(request, f'{model_name} successfully deleted.')
    return redirect('/')


    #return render(request, 'delete_items.html')


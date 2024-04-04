from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def cleanUser(self):
        cleaned_user = super().clean()
        # check each field individually
        for field in self.Meta.fields:
            if not cleaned_user.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_user

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'address']

    def cleanCustomer(self):
        cleaned_customer = super().clean()
        # check each field individually
        for field in self.Meta.fields:
            if not cleaned_customer.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_customer

class VehicleCreate(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['model', 'make', 'year', 'price_per_day', 'is_available']

    def cleanVehicle(self):
        cleaned_vehicle = super().clean()
        #check each field individually
        for field in self.Meta.fields:
            if not cleaned_vehicle.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_vehicle

class BookingCreate(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'vehicle', 'start_date', 'end_date', 'total_cost']

    def cleanBooking(self):
        cleaned_booking = super().clean()
        #check each field individually
        for field in self.Meta.fields:
            if not cleaned_booking.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_booking

class FleetCreate(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = ['name', 'vehicles']

    def cleanFleet(self):
        cleaned_fleet = super().clean()
        #check each field individually
        for field in self.Meta.fields:
            if not cleaned_fleet.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_fleet

class InventoryCreate(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['vehicle', 'quantity']

    def cleanInventory(self):
        cleaned_inventory = super().clean()
        #check each field individually
        for field in self.Meta.fields:
            if not cleaned_inventory.get(field):
                raise forms.ValidationError(f"{field.replace('_', ' ').title()} field is required.")
        return cleaned_inventory

class SearchFormCustomer(forms.Form):
    make = forms.ChoiceField(choices=Vehicle.MAKE_CHOICES)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()

class BookingFormCustomer(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']

class VehicleSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Vehicle
        fields = ['model', 'make']

class BookingSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Booking
        fields = ['customer', 'vehicle']

class FleetSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Fleet
        fields = ['name']

class InventorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Inventory
        fields = ['vehicle']
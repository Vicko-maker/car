from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Vehicle(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Honda', 'Honda'),
        ('Nissan', 'Nissan'),
        ('BMW', 'BMW'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Volkswagen', 'Volkswagen'),
        ('Audi', 'Audi'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Lexus', 'Lexus'),
        ('Subaru', 'Subaru'),
        ('Mazda', 'Mazda'),
        ('Dodge', 'Dodge'),
        ('Porsche', 'Porsche'),
        ('Jeep', 'Jeep'),
        ('Cadillac', 'Cadillac'),
        ('Tesla', 'Tesla'),
        ('Volvo', 'Volvo'),
        ('Land Rover', 'Land Rover'),
        ('Jaguar', 'Jaguar'),
        ('Acura', 'Acura'),
        ('Infiniti', 'Infiniti'),
        ('Mini', 'Mini'),
        ('Buick', 'Buick'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Chrysler', 'Chrysler'),
        ('Fiat', 'Fiat'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Bentley', 'Bentley'),
        ('Aston Martin', 'Aston Martin'),
        ('Lamborghini', 'Lamborghini'),
        ('Ferrari', 'Ferrari'),
        ('Maserati', 'Maserati'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('McLaren', 'McLaren'),
        ('Pagani', 'Pagani'),
        ('Bugatti', 'Bugatti')
    ]

    model = models.CharField(max_length=100)
    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=400)
    end_date = models.CharField(max_length=400)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vehicle} booked by {self.customer}"


class Fleet(models.Model):
    name = models.CharField(max_length=100)
    vehicles = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.vehicle} - {self.quantity} available"


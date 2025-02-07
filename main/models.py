from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class User(User):
    phone_number = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.username

class CarsModel(models.Model):
    CAR_CATERGORY =[
        ('Family', 'Family'),
        ('Sport Car', 'Sport Car'),
        ('Lux', 'Lux'),
        ('Business', 'Business')
    ]
    name = models.CharField(max_length=128)
    car_type = models.CharField(max_length=128)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    car_category = models.CharField(max_length=64, choices=CAR_CATERGORY
                                    ,default="Family")
    is_available = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.is_available}"

class RentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rental')
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='rental')
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(null=True, blank=True)
    total_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.email} - {self.car.name} - {self.car.car_category}"
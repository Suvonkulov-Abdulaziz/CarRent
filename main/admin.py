from django.contrib import admin
from .models import User, CarsModel, RentModel
# Register your models here.
@admin.register(User)
@admin.register(CarsModel)
@admin.register(RentModel)
class User(admin.ModelAdmin):
    pass
class CarsModel(admin.ModelAdmin):
    pass
class RentModel(admin.ModelAdmin):
    pass

from django.shortcuts import render, redirect
from .models import CarsModel

# Create your views here.
def MainView(request):
    Cars = CarsModel.objects.all
    context = {
        'CarsModel': Cars
    }
    return render(request, "index.html", context=context)
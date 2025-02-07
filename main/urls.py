from django.urls import path
from .views import MainView
urlpatterns = [
    path('', MainView, name='main'),
]
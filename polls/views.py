from django.shortcuts import render, get_object_or_404
from .models import Car

def index(request):
    cars = Car.objects.all() # Bazadakı bütün maşınları çəkirik
    return render(request, 'polls/index.html', {'cars': cars})

def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id) # Seçilən ID-yə uyğun maşını tapırıq
    return render(request, 'polls/detail.html', {'car': car})
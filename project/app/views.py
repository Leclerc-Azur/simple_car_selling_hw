from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Category
from django import forms
from django.contrib.auth.decorators import login_required

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'model', 'year', 'image', 'price', 'description', 'category']

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'app/add_car.html', {'form': form})

def index_view(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'app/car_detail.html', {'car': car})
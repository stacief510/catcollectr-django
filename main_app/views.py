from django.shortcuts import render
from .models import Cat
# from django.http import HttpResponse
# Create your views here.

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', { 'cats': cats})



# def index(request):
#     return render(request, 'index.html', {'cats': cats})

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age



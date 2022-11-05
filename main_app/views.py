from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Finch


# Create your views (controllers) here.

# Home
def home(request):
  return render(request, 'home.html')

# About page
def about(request):
  return render(request, 'about.html')

# View all finches
def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

# View the details of a finch
def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

# Creating a finch
class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

## The above is the same as 
# class FinchCreate(CreateView):
#   model = Finch
#   fields = ['name', 'breed', 'description', 'age']
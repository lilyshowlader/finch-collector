from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm


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
  # Get the toys the finch doesn't have
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    # Add the toys to be displayed
    'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have
  })




# Creating a finch
class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

# Updating a finch
class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

# Deleting a finch
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

# Adding a feeding for a finch
def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finches_detail', finch_id=finch_id)


# Creating a toy
class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

# View list of toys
class ToyList(ListView):
  model = Toy

# View detail of toy
class ToyDetail(DetailView):
  model = Toy

# Update the toy
class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

# Delete the toy
class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

# Associating the toy
def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finches_detail', finch_id=finch_id)
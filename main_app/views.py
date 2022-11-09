from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Finch, Toy
from .forms import FeedingForm


# Create your views (controllers) here.

# Home
class Home(LoginView):
  template_name = 'home.html'

# About page
def about(request):
  return render(request, 'about.html')

# View all finches
@login_required
def finches_index(request):
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'finches/index.html', { 'finches': finches })

# View the details of a finch
@login_required
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
class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

  # This inherited method is called when a valid finch form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the finch
    # Let the CreateView do its job as usual
    return super().form_valid(form)


# Updating a finch
class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

# Deleting a finch
class FinchDelete(LoginRequiredMixin, DeleteView):
  model = Finch
  success_url = '/finches/'

# Adding a feeding for a finch
@login_required
def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finches_detail', finch_id=finch_id)


# Creating a toy
class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

# View list of toys
class ToyList(LoginRequiredMixin, ListView):
  model = Toy

# View detail of toy
class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

# Update the toy
class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

# Delete the toy
class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

# Associating the toy
@login_required
def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finches_detail', finch_id=finch_id)


# Signing up a user
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('finches_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})
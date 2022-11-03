from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Queens', 'cool finchie', 'very cool.', 3),
  Finch('Manhattan', 'nice finchie', 'likes espresso martinis', 0),
  Finch('Brooklyn', 'pleasant finchie', 'stylish', 4),
  Finch('Bronx', 'happy finchie', 'sleepy', 6)
]


# Create your views (controllers) here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })
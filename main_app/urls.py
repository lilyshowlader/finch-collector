from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  # localhost:8000/about
  path('about/', views.about ,name='about'),
  # localhost:8000/finches
  path('finches/', views.finches_index, name='finches_index'),
]
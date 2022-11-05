from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),
  # localhost:8000/about
  path('about/', views.about ,name='about'),
  # localhost:8000/finches
  path('finches/', views.finches_index, name='finches_index'),

  # viewing a single finch details finch
  # localhost:8000/finch/int:finch_id
  path('finches/<int:finch_id>/',views.finches_detail, name='finches_detail'),

  # to create a cat
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
]
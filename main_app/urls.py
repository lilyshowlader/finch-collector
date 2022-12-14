from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.Home.as_view(), name='home'),

  # localhost:8000/about
  path('about/', views.about ,name='about'),

  # localhost:8000/finches
  path('finches/', views.finches_index, name='finches_index'),

  # localhost:8000/finch/int:finch_id (to view the details of a single finch)
  path('finches/<int:finch_id>/',views.finches_detail, name='finches_detail'),

  # localhost:8000/finches/create
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),

  # localhost:8000/finches/int:finch_id/update
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),

  # localhost:8000/finchess/int:finch_id/delete
  path('finchess/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),

  # localhost:8000/finchess/int:finch_id/add_feeding
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),

  # localhost:8000/toys/create
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),

  # toys
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),

  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

  # Associate a toy with a Finch (M:M)
  path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

  # Sign up a user
  path('accounts/signup/', views.signup, name='signup'),
  ]

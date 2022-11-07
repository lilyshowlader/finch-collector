from django.urls import path
from . import views

urlpatterns = [
  # localhost:8000/
  path('', views.home, name='home'),

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
]
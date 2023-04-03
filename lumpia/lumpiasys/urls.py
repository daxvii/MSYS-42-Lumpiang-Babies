from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit_productlist/', views.edit_productlist, name='edit_productlist'),
    path('create_product/', views.create_product, name='create_product'),
    path('view_product/<int:pk>/', views.view_product, name='view_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('inventory_tally/', views.inventory_tally, name='inventory_tally'),
    path('import_sales/', views.import_sales, name='import_sales'),
    path('remaining_inventory/', views.remaining_inventory, name='remaining_inventory'),
    path('confirm_sales/', views.confirm_sales, name='confirm_sales'),
    path('confirm_inventory/', views.confirm_inventory, name='confirm_inventory'),
]
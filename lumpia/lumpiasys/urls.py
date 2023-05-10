from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home'),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_productlist/', views.edit_productlist, name='edit_productlist'),
    path('view_product/<int:pk>/', views.view_product, name='view_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('inventory_tally/', views.inventory_tally, name='inventory_tally'),
    path('import_sales/', views.import_sales, name='import_sales'),
    path('remaining_inventory/', views.remaining_inventory, name='remaining_inventory'),
    path('confirm_sales/', views.confirm_sales, name='confirm_sales'),
    path('confirm_inventory/', views.confirm_inventory, name='confirm_inventory'),
    path('create_group/', views.create_group, name='create_group'),
    path('edit_grouplist/', views.edit_grouplist, name='edit_grouplist'),
    path('view.group/<int:pk>/', views.view_group, name='view_group'),
    path('update_group/<int:pk>/', views.update_group, name='update_group'),
    path('delete_group/<int:pk>/', views.delete_group, name='delete_group'),
    path('create_combo/', views.create_combo, name='create_combo'),
    path('view_combo/<int:pk>/', views.view_combo, name='view_combo'),
    path('update_combo/<int:pk>/', views.update_combo, name='update_combo'),
    path('delete_combo/<int:pk>/', views.delete_combo, name='delete_combo'),
    path('inventory_records_by_date/', views.inventory_records_by_date, name='inventory_records_by_date'),
]
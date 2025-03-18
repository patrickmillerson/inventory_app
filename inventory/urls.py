from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('add_category/', views.add_category, name='add_category'),
    path('category_list/', views.category_list, name='category_list'),
    path('category/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('items_list/', views.items_list, name='items_list'),
    path('add-item/', views.add_item, name='add_item'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('item/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
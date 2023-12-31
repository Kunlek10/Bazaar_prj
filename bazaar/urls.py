from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path("buy", views.Buy, name="buy"),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]

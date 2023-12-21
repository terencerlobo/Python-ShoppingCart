from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart_items/', CartItemViews.as_view())
]
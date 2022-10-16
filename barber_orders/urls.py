from django.urls import path
from .views import OrderCreate
#from .views import order_create

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),
]
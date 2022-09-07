from django.urls import path

from .views import ShopListView

urlpatterns = [
    path('', ShopListView.as_view(), name='main_page'),
]
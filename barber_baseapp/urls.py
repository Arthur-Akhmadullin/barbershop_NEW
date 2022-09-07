from django.urls import path

from .views import NewsListView, NewsDetailView, PriceListView, MainPage, RecordCreate


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('news/', NewsListView.as_view(), name='news_page'),
    path('news/<str:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('price/', PriceListView.as_view(), name='price_page'),
    path('record_created/', RecordCreate.as_view(), name='record'),
]
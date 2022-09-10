from django.urls import path

from .views import ShopListView, ShopProductGroupView, ShopFilter, ShopDetailView

urlpatterns = [
    path('', ShopListView.as_view(), name='shop_page'),
    path('filter/', ShopFilter.as_view(), name='shop_filter'),
    path('<str:group_slug>/', ShopProductGroupView.as_view(), name='shop_page_by_groups'),
    path('<str:group_slug>/<str:slug>/', ShopDetailView.as_view(), name='shop_detail_page'),
]
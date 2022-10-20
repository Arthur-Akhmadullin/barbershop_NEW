from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductGroup
from .utils import ShopMixin
from barber_cart.forms import CartAddProductForm


class ShopListView(ShopMixin, ListView):
    model = Product
    template_name = 'barber_shop/shop.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context.update(self.get_filter_context())
        context.update(self.get_pagination_parameters())
        return context


class ShopProductGroupView(ShopMixin, ListView):
    model = Product
    template_name = 'barber_shop/shop.html'
    context_object_name = 'products'
    paginate_by = 3
    slug_url_kwarg = 'group_slug'

    def get_context_data(self, **kwargs):
        context = super(ShopProductGroupView, self).get_context_data(**kwargs)
        context.update(self.get_filter_context())
        context.update(self.get_pagination_parameters())
        context['selected_group'] = get_object_or_404(ProductGroup,
                                                      slug__iexact=self.kwargs['group_slug']
                                                      )
        return context

    def get_queryset(self):
        return Product.objects.filter(group__slug__iexact=self.kwargs['group_slug'])


class ShopFilter(ShopMixin, ListView):
    template_name = 'barber_shop/shop.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ShopFilter, self).get_context_data(**kwargs)
        context.update(self.get_filter_context())
        context.update(self.get_pagination_parameters())

        filter_check_points = {}
        if self.request.GET.getlist("product_name"):
            filter_check_points.update(name=self.request.GET.getlist("product_name"))
        if self.request.GET.get("product_group"):
            filter_check_points.update(group=int(self.request.GET.get("product_group")))
        context['filter_check_points'] = filter_check_points
        return context

    def get_queryset(self):
        self.queryset = Product.objects.all()
        if self.request.GET.get("product_group"):
            self.queryset = Product.objects.filter(group=self.request.GET.get('product_group'))

        if self.request.GET.getlist("product_name"):
            self.queryset = self.queryset.filter(name__manufacturer__in=self.request.GET.getlist("product_name"))
        return self.queryset


class ShopDetailView(DetailView):
    model = Product
    template = 'barber_shop/product_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_object(self):
        return get_object_or_404(Product,
                                 group__slug__iexact=self.kwargs['group_slug'],
                                 slug__iexact=self.kwargs['slug']
                                 )
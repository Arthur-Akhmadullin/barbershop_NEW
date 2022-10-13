from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from barber_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartAdd(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart_detail')


class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})
        return render(request, 'barber_cart/cart_detail.html', {'cart': cart})


class CartRemove(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart_detail')




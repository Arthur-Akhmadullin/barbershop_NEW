from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCreateForm
from barber_cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_create_form = OrderCreateForm(request.POST)
        if order_create_form.is_valid():
            order = order_create_form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )

            # Очищаем корзину.
            cart.clear()
            # order_created(order.id)
            # if request.user.is_authenticated:
            #     user = User.objects.get(id=request.user.id)
            #     profile = Profile.objects.filter(user=user).get()
            #     order.profile = profile
            #     order.save()
            return render(request, 'barber_orders/order_created.html', {'order': order})
    else:
        order_create_form = OrderCreateForm()
    return render(request, 'barber_orders/order_create.html', {'cart': cart,
                                                               'order_create_form': order_create_form})
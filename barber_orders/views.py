from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic import View

from .models import Order, OrderItem
from barber_account.models import Profile
from .forms import OrderCreateForm
from barber_cart.cart import Cart


class OrderCreate(View):
    def post(self, request):
        cart = Cart(request)
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
            self.order_created(order.id)
            if request.user.is_authenticated:
                user = User.objects.get(id=request.user.id)
                profile = Profile.objects.filter(user=user).get()
                order.profile = profile
                order.save()
            return render(request, 'barber_orders/order_created.html', {'order': order})

    def get(self, request):
        cart = Cart(request)
        order_create_form = OrderCreateForm()
        return render(request, 'barber_orders/order_create.html', {'cart': cart,
                                                                   'order_create_form': order_create_form})


    def order_created(self, order_id):
        """Задача отправки email-уведомлений при успешном оформлении заказа."""
        order = Order.objects.get(id=order_id)
        subject = 'Ордер № {}'.format(order.id)
        message = 'Товарищ {},\n\nВы успешно создали заказ.\Ваш заказ -№{}.'.format(order.first_name, order.id)
        mail_sent = send_mail(subject, message, 'barbershop.django@mail.ru', [order.email])
        return mail_sent
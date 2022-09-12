from django.db import models
from barber_shop.models import Product
from barber_account.models import Profile


class Order(models.Model):
    NO_PAID = 0
    PAID = 1
    SENT = 2
    DELIVERED = 3

    STATUS_CHOICES = ((NO_PAID, 'Не оплачено'),
                      (PAID, 'Оплачено'),
                      (SENT, 'Отправлено'),
                      (DELIVERED, 'Доставлено')
                      )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    user_comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NO_PAID)
    #paid = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', 	on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


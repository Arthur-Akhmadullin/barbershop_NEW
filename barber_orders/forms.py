from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    '''Форма для заказа и оформления товаров'''
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'user_comment']

        '''
        Для примера, стили TextInput и TextArea не стал указывать в widgets через attrs.
        В файле order_create.html каждое поле формы заключил в div с классом order-form.
        Таким образом, вид не поменялся, но необходимость прописывать класс каждого поля отпала. 
        '''
        widgets = {
            'user_comment': forms.Textarea(),
        }

        labels = {
            'first_name': ('Имя'),
            'last_name': ('Фамилия'),
            'email': ('Электронная почта'),
            'address': ('Адрес доставки'),
            'phone': ('Телефон'),
            'user_comment': ('Комментарий к заказу'),
        }
from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    '''Форма для заказа и оформления товаров'''
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'user_comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'display:block;' 
                                                    'width:200px;' 
                                                    'padding-left: 10px;' 
                                                    'padding-top:5px;' 
                                                    'padding-bottom:5px;' 
                                                    'font-size: 18px;'}),
            'last_name': forms.TextInput(attrs={'style': 'display:block;' 
                                                   'width:200px;' 
                                                   'padding-left: 10px;' 
                                                   'padding-top:5px;' 
                                                   'padding-bottom:5px;' 
                                                   'font-size: 18px;'}),
            'email': forms.TextInput(attrs={'style': 'display:block;' 
                                               'width:200px;' 
                                               'padding-left: 10px;' 
                                               'padding-top:5px;' 
                                               'padding-bottom:5px;' 
                                               'font-size: 18px;'}),
            'address': forms.TextInput(attrs={'style': 'display:block;' 
                                                 'width:200px;' 
                                                 'padding-left: 10px;' 
                                                 'padding-top:5px;' 
                                                 'padding-bottom:5px;' 
                                                 'font-size: 18px;'}),
            'phone': forms.TextInput(attrs={'style': 'display:block;' 
                                               'width:200px;' 
                                               'padding-left: 10px;' 
                                               'padding-top:5px;' 
                                               'padding-bottom:5px;' 
                                               'font-size: 18px;'}),
            'user_comment': forms.Textarea(attrs={'style': 'display:block;'
                                                            'width:200px;'
                                                            'height:150px;'
                                                            'padding-left: 10px;'
                                                            'padding-top:5px;'
                                                            'padding-bottom:5px;'
                                                            'font-size: 18px;'}),
        }
        labels = {
            'first_name': ('Имя'),
            'last_name': ('Фамилия'),
            'email': ('электронная почта'),
            'address': ('Адрес доставки'),
            'phone': ('Телефон'),
            'user_comment': ('Комментарий к заказу'),
        }
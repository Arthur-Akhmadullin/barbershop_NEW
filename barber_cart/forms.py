from django import forms
# from django.forms import TextInput
# from .models import Order, Profile, Record
#
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # Корзина
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label="")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    #Полю select присваиваем css-класс, чтобы он нормально отображался на странице товара
    quantity.widget.attrs.update({'style': 'display:inline-block;' 
                                           'box-sizing: content-box;' 
                                           'border-radius:2px;'
                                           'padding-left: 10px;' 
                                           'width: 90px;' 
                                           'height:42px;' 
                                           'font-size: 18px;'
                                           'font-weight:700;' 
                                           'text-align:center;'
                                  })
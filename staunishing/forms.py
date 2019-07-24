from django import forms

from staunishing.models import *

class CartForm(forms.ModelForm):
    class Meta():
        model=Cart
        fields=['count']


class CheckoutForm(forms.ModelForm):
    class Meta():
        model=Checkout
        fields='__all__'
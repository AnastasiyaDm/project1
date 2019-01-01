from django import forms
from django.forms import ModelForm
from .models.order import Order
from .models.pizza import Pizza
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegForm(forms.Form):
    username = forms.CharField( label='Username',
                                max_length=100,
                                widget= forms.TextInput(
                                    attrs={'class':'form-control'}
                                ))
    email = forms.EmailField(widget= forms.TextInput(
                                    attrs={'class':'form-control'}
                                ))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields=['pizza','name','phone','address']
        widgets= {
        'pizza':forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Order'))

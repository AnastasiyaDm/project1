from django import forms

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

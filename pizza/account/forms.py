from django.forms import ModelForm
from account.models import Profile
from django.contrib.auth.models import User

class CustomerRegForm(ModelForm):
    'Profile registration model form'
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

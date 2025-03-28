from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField(label=_('Postal code'))
    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.HiddenInput,
        required=False
    )
    
    class Meta:
        model = Order
        fields = ['user', 'first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

from django import forms
from django.contrib.auth.models import User
from django.db.models import get_model


class RecipientForm(forms.ModelForm):
    """
    Form class for choosing recipients for the contact form in the admin site.
    """
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True))

    class Meta:
        model = get_model('contact_form', 'contactrecipient')

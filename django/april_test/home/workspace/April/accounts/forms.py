from django import forms
from django.contrib.auth.models import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationForm(forms.UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
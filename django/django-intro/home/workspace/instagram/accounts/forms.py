from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.conf import settings
from .models import Profile

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email',)
        
class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
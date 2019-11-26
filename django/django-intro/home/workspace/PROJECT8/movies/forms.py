from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie

# modelform
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('Submit', '제출!'))
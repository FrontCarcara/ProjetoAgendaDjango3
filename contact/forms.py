from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForms(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )         
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)
            
    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError(
                'Priemiro nome não pode ser igual ao segundo',
                code='invalid'
            )    
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
             ValidationError(
                    'Mensagem de  add_error',
                code='invalid'
            )
        )
        return first_name

class RegisterForm(UserCreationForm):
    ...
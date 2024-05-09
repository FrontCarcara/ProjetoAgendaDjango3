from typing import Any

from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)
        
    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()

# Create your views here.
def create(request):
    if request.method == 'POST':

    
        context = {
            'form': ContactForms(request.POST),
            }

        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
        'form': ContactForms(),
        }

    return render(
        request,
        'contact/create.html',
        context,
    )


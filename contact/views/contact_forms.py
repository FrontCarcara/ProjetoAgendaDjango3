from typing import Any

from django.shortcuts import render

from contact.forms import ContactForms


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


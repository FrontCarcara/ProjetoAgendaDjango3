from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects \
        .filter (show=True) \
        .order_by('-id')[10:20]

    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
        }

    return render(
        request,
        'contact/index.html',
        context,
    )

  
def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')
    
    print(search_value) 
    
    
    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)   
        )\
        .order_by('-id')

    print(contacts.query)
    
    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        }

    return render(
        request,
        'contact/index.html',
        context,
    )

  

def contact(request, contact_id):
    #single_contact = Contact.objects.filter(id=contact_id).first()
    #if single_contact is None:
        #raise Http404()
    
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title,
        
        }

    return render(
        request,
        'contact/contact.html',
        context,
    )
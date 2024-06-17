from django.shortcuts import render, redirect

from contact.forms import ContactMessageForm
from contact.models import ContactMessage, Category


# Create your views here.
def contact_view(request):
    ctx = {
        'messages': ContactMessage.objects.all(),
        'categories': Category.objects.all(),
        'form': ContactMessageForm()
    }
    return render(request, 'contact/index.html', context=ctx)


def page_gratitude_view(request, contact_id):
    ctx = {
        'messages': ContactMessage.objects.get(id=contact_id),
    }
    return render(request, 'contact/page_gratitude.html', context=ctx)


def add_contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
        return redirect('page_gratitude_view', contact_id=contact.id)
    return redirect('contact_view')

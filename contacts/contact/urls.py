from django.urls import path

from contact.views import contact_view, add_contact, page_gratitude_view

urlpatterns = [
    path('', contact_view, name='contact_view'),
    path('add_contact', add_contact, name='add_contact'),
    path('page_gratitude_view/<int:contact_id>', page_gratitude_view, name='page_gratitude_view'),
]

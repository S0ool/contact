from django import forms

from contact.models import Category, ContactMessage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

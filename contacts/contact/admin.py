from django.contrib import admin

from contact.models import Category, ContactMessage

admin.site.register(Category)
admin.site.register(ContactMessage)

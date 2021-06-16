from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'title', 'created',)
    list_filter = ('first_name', 'created')
    search_fields = ['first_name', ]


admin.site.register(Contact, ContactAdmin)

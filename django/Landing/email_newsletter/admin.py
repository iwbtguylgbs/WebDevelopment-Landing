from django.contrib import admin
from .models import PeopleList

# Register your models here.

class PeopleListAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mail", "number")
    list_display_links = ("id", "name", "mail", "number")

admin.site.register(PeopleList, PeopleListAdmin)
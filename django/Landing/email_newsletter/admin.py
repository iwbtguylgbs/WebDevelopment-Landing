from django.contrib import admin
from .models import PeopleList, PlatformsList

# Register your models here.

class PeopleListAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "mail", "number")
    list_display_links = ("id", "name", "age", "mail", "number")

class PlatformListAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "number", "adresses")
    list_display_links = ("id", "city", "number", "adresses")

admin.site.register(PeopleList, PeopleListAdmin)
admin.site.register(PlatformsList, PlatformListAdmin)
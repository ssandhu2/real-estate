from django.contrib import admin

from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date') #display in /admin all column name
    list_display_links = ('id', 'name') #click on title and id for details
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

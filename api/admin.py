from django.contrib import admin

from .models import test

class testadmin(admin.ModelAdmin):
    list_display = ('name', 'age')

admin.site.register(test, testadmin)

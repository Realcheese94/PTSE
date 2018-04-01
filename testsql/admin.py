from django.contrib import admin
from .models import SUser
# Register your models here.

@admin.register(SUser)
class SUseradmin(admin.ModelAdmin):
    list_display = ['SuserId','Susername','Susertel']

from django.contrib import admin

from .models import Var


@admin.register(Var)
class VarAdmin(admin.ModelAdmin):
    search_fields = ['name', 'value', 'user__username']
    list_filter = ['owner', 'name']
    list_display = ['name', 'value', 'owner']

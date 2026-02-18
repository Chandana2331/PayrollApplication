from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'created_at')
    search_fields = ('name', 'registration_number')
    readonly_fields = ('id', 'created_at', 'updated_at')

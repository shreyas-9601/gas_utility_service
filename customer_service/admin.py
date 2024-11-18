from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('customer_name', 'service_type', 'email')
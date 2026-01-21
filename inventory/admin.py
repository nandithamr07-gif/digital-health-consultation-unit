from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_number', 'quantity', 'low_stock_threshold', 'last_refilled')
    list_filter = ('last_refilled',)
    search_fields = ('name', 'batch_number')

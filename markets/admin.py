from django.contrib import admin
from .models import Market

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = (
        'market_name',
        'market_work_time',
        'market_phone',
        'market_grill',
        'manager_full_name',
        'manager_work_time',
        'manager_day_off',
        'manager_phone',
        'supervisor_one_full_name',
        'supervisor_one_phone',
        'supervisor_one_work_time',
        'supervisor_one_day_off',
        'supervisor_two_full_name',
        'supervisor_two_phone',
        'supervisor_two_work_time',
        'supervisor_two_day_off',
        'additional_info'
    )
    search_fields = ('market_name', 'manager_full_name')  # Поля для поиска
    list_filter = ('manager_day_off', 'supervisor_one_day_off', 'supervisor_two_day_off')  # Фильтры

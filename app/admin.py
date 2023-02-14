from django.contrib import admin

# Register your models here.

from .models import TGClient, Pricing, Balance

class TGClientAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'created_at')

class PricingAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price', 'link')

class BalanceAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'tariff', 'next_payment', 'created_at')

admin.site.register(TGClient, TGClientAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Balance, BalanceAdmin)
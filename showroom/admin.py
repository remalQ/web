from django.contrib import admin
from models import Car, Sale, TradeINDeal

# Регистрируем модели в админке для удобного управления


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'is_new')
    search_fields = ('make', 'model')
    list_filter = ('is_new', 'year')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'client', 'date_of_sale', 'is_tradein')
    search_fields = ('client__username', 'car__make', 'car__model')


@admin.register(TradeINDeal)
class TradeINDealAdmin(admin.ModelAdmin):
    list_display = ('client', 'old_car_description', 'new_car', 'valuation', 'final_price')
    search_fields = ('client__username', 'new_car__make', 'old_car_description')

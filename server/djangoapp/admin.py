from django.contrib import admin
from .models import CarMake,CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1
# CarModelAdmin class
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'name', 'car_type', 'year', 'dealer_id')
    search_fields = ('name', 'car_type', 'year', 'dealer_id')
# CarMakeAdmin class with CarModelInline
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CarModelInline]
# Register models here

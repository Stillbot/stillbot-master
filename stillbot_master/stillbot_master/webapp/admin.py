from django.contrib import admin
from models import Thermistor, Temperature


class ThermistorAdmin(admin.ModelAdmin):
    list_display = ('model', 'index', 'name', 'latest_temp', 'description')


class TemperatureAdmin(admin.ModelAdmin):
    list_display = ('thermistor', 'temp', 'created_on')
    list_filter = ('thermistor', )

admin.site.register(Thermistor, ThermistorAdmin)
admin.site.register(Temperature, TemperatureAdmin)

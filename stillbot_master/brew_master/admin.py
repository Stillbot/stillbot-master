from django.contrib import admin
from stillbot_master.brew_master.models import *


class YieldAdminInline(admin.StackedInline):
    model = Yield


class WashAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'starting_sg', 'ended_sg', 'pitching_temp', )
    fields = ('name', 'ingredients', 'starting_sg', 'ended_sg', 'procedure', 'created_on', 'pitching_temp', 'starting_ph', 'ending_ph', )
    readonly_fields = ('created_on', )
    inlines = (YieldAdminInline, )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'place_of_origin', )
    fields = list_display + ('barcode', )


class IngredientMeasurementAdmin(admin.ModelAdmin):
    fields = list_display = ('ingredient', 'amount', 'measurement', )


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'address', 'contact', )
    fields = list_display


admin.site.register(Wash, WashAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientMeasurement, IngredientMeasurementAdmin)
admin.site.register(Place, PlaceAdmin)

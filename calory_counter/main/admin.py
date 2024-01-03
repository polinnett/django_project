from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Vegetable, Fruit, Meat, Grain, Profile, Record
from import_export.admin import ExportActionModelAdmin
from import_export import resources


class RecordResource(resources.ModelResource):
    class Meta:
        model = Record

class RecordAdmin(ExportActionModelAdmin):
    resource_class = RecordResource


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'calories', 'proteins', 'fats', 'carbohydrates']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name', 'calories', 'proteins', 'fats', 'carbohydrates']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'age', 'height', 'weight', 'photo', 'reg_date']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name', 'age', 'height', 'weight']
    date_hierarchy = 'reg_date'


class RecordAdmin(SimpleHistoryAdmin):
    filter_horizontal = ('veg_id', 'fruit_id', 'meat_id', 'grain_id')
    raw_id_fields = ['user_id']


admin.site.register(Vegetable, ProductsAdmin)
admin.site.register(Fruit, ProductsAdmin)
admin.site.register(Meat, ProductsAdmin)
admin.site.register(Grain, ProductsAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Record, RecordAdmin)

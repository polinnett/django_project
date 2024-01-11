from django.contrib import admin
from import_export.formats import base_formats
from simple_history.admin import SimpleHistoryAdmin

from .models import Vegetable, Fruit, Meat, Grain, Profile, Record
from import_export.admin import ImportExportMixin
from import_export import resources, fields
from datetime import datetime

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'calories', 'proteins', 'fats', 'carbohydrates']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name', 'calories', 'proteins', 'fats', 'carbohydrates']

class CustomExportImportMixin(ImportExportMixin):
    def get_export_filename(self, request, queryset, file_format):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = "%s-%s.%s" % (
            self.model.__name__,
            date_str,
            file_format.get_extension(),
        )
        return filename
    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLSX
        )
        return [f for f in formats if f().can_export()]

class FruitResource(resources.ModelResource):
    title = fields.Field()
    class Meta:
        model = Fruit
    def dehydrate_title(self, fruit):
        name = getattr(fruit, "name", "unknown")
        calories = getattr(fruit, "calories", "unknown")
        return "%s содержит %s калорий" % (
            name,
            calories
        )

class FruitAdmin(CustomExportImportMixin, ProductsAdmin):
    resource_class = FruitResource

class VegetableResource(resources.ModelResource):
    class Meta:
        model = Vegetable

class VegetableAdmin(CustomExportImportMixin, ProductsAdmin):
    resource_class = VegetableResource

class MeatResource(resources.ModelResource):
    class Meta:
        model = Meat

class MeatAdmin(CustomExportImportMixin, ProductsAdmin):
    resource_class = MeatResource

class GrainResource(resources.ModelResource):
    class Meta:
        model = Grain

class GrainAdmin(CustomExportImportMixin, ProductsAdmin):
    resource_class = GrainResource


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'age', 'height', 'weight', 'photo', 'reg_date', 'is_active']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name', 'age', 'height', 'weight']
    date_hierarchy = 'reg_date'
    ordering = ['height']


class RecordResource(resources.ModelResource):
    name = fields.Field()
    class Meta:
        model = Record
    def dehydrate_name(self, record):
        user_id = getattr(record, "user_id", "unknown")
        return user_id.name
class RecordAdmin(CustomExportImportMixin, SimpleHistoryAdmin):
    filter_horizontal = ('veg_id', 'fruit_id', 'meat_id', 'grain_id')
    raw_id_fields = ['user_id']
    resource_class = RecordResource


admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Meat, MeatAdmin)
admin.site.register(Grain, GrainAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Record, RecordAdmin)


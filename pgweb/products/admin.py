from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import Product, ProductSection, ProductFeatureGrid, ProductFeatureGridObject

class ProductSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')

class ProductFeatureGridAdmin(admin.ModelAdmin):
    list_display = ('section_name', 'product')

class ProductFeatureGridObjectAdmin(admin.ModelAdmin):
    list_display =('name', 'feature_grid')

admin.site.register(Product)
admin.site.register(ProductSection, ProductSectionAdmin)
admin.site.register(ProductFeatureGrid, ProductFeatureGridAdmin)
admin.site.register(ProductFeatureGridObject, ProductFeatureGridObjectAdmin)

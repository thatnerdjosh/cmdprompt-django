from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import Product, ProductSection, ProductFeatureGrid, ProductFeatureGridObject

class ProductSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')

admin.site.register(Product)
admin.site.register(ProductSection, ProductSectionAdmin)
admin.site.register(ProductFeatureGrid)
admin.site.register(ProductFeatureGridObject)

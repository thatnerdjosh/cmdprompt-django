from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import Product, ProductSection, ProductFeatureGrid, ProductFeatureGridObject

admin.site.register(Product)
admin.site.register(ProductSection)
admin.site.register(ProductFeatureGrid)
admin.site.register(ProductFeatureGridObject)

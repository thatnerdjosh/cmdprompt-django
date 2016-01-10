from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import Service, PackageService

admin.site.register(Service)
admin.site.register(PackageService)

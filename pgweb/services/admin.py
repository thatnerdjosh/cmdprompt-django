from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import Service, ServiceSection, PackageService, ProfessionalService, CloudService

class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'service')

admin.site.register(PackageService)
admin.site.register(ProfessionalService)
admin.site.register(CloudService)
admin.site.register(Service)
admin.site.register(ServiceSection, ServiceSectionAdmin)

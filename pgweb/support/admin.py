from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import SupportPage, SupportPageSection

admin.site.register(SupportPage)
admin.site.register(SupportPageSection)

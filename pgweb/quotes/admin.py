from django.contrib import admin
from models import Quote

class QuoteAdmin(admin.ModelAdmin):
	list_display = ('quote', 'who', 'org', 'feature' )

admin.site.register(Quote, QuoteAdmin)

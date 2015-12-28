from django.contrib import admin
from pgweb.util.admin import PgwebAdmin
from models import TeamMember, AboutContentBlock

class TeamMemberAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)


admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(AboutContentBlock)

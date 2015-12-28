from models import BlogPost
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(BlogPost, BlogAdmin)

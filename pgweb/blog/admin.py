from models import BlogPost, BlogPostCategoryRelationship, Category
from django.contrib import admin

class BlogPostCategoryRelationshipInline(admin.TabularInline):
    model = BlogPostCategoryRelationship
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = (BlogPostCategoryRelationshipInline,)
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.TextField()
    url_slug = models.TextField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, blank=True, null=True)
    active = models.BooleanField(default=False)
    body = HTMLField()
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    list_on_side = models.BooleanField(default=False)
    featured = models.BooleanField(default=False, help_text="Main featured blog post (we can only have one)")
    feature_image = models.ImageField(default=None, blank=True, null=True, upload_to = 'images/featured_blog', help_text="Image to be displayed when the blog is featured on the home page")

    def __unicode__(self):
	    return self.title

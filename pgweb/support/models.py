from django.db import models
from tinymce.models import HTMLField

class SupportPage(models.Model):
    name = models.TextField()
    url_slug = models.TextField()
    description = HTMLField()

    def __unicode__(self):
        return self.name

class SupportPageSection(models.Model):
    section_name = models.TextField()
    support_page = models.ForeignKey(SupportPage, blank=True, null=True)
    content = HTMLField()

    def __unicode__(self):
        return self.name

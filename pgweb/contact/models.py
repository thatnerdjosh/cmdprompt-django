from django.db import models
from tinymce.models import HTMLField

class ContactSection(models.Model):
    name = models.TextField()
    description = HTMLField()

    def __unicode__(self):
        return self.name

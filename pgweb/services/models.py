from django.db import models
from tinymce.models import HTMLField

class Service(models.Model):
    name = models.TextField()
    url_slug = models.TextField(unique=True)
    description = models.TextField()

    def __unicode__(self):
	    return self.name

class ServiceSection(models.Model):
    name = models.TextField()
    description = HTMLField()
    service = models.ForeignKey(Service, blank=True, null=True)

    def __unicode__(self):
        return self.name

class PackageService(models.Model):
    name = models.TextField()
    link = models.TextField(unique=True)
    description = models.TextField()

    def __unicode__(self):
	    return self.name

class ProfessionalService(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

class CloudService(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

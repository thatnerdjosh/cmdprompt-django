from django.db import models

class Service(models.Model):
    name = models.TextField()
    url_slug = models.TextField(unique=True)
    description = models.TextField()

    def __unicode__(self):
	    return self.name

class PackageService(models.Model):
    name = models.TextField()
    link = models.TextField(unique=True)
    description = models.TextField()

    def __unicode__(self):
	    return self.name

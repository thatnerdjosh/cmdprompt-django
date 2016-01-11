from django.db import models
from tinymce.models import HTMLField

class Product(models.Model):
    name = models.TextField()
    url_slug = models.TextField(unique=True)
    description = models.TextField()
    picture = models.ImageField(upload_to = 'images/product', help_text="Dimensions must be equal, ex: 100x100")
    short_description = models.TextField()

    def __unicode__(self):
	    return self.name

class ProductSection(models.Model):
    name = models.TextField()
    description = HTMLField()
    product = models.ForeignKey(Product, blank=True, null=True)

    def __unicode__(self):
        return self.name

class ProductFeatureGrid(models.Model):
    section_name = models.TextField()
    product = models.ForeignKey(Product, blank=True, null=True)

    def __unicode__(self):
        return self.section_name

class ProductFeatureGridObject(models.Model):
    name = models.TextField()
    description = models.TextField()
    feature_grid = models.ForeignKey(ProductFeatureGrid, blank=True, null=True)

    def __unicode__(self):
        return self.name

from django.db import models
from tinymce.models import HTMLField

class TeamMember(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
							help_text="Team Member Name")
    title = models.CharField(max_length=100, null=False, blank=False,
							help_text="Team Member Role")
    profile_pic = models.ImageField(upload_to = 'media/images/team', help_text="Dimensions must be equal, ex: 100x100")
    bio = models.TextField(null=False)

    def __unicode__(self):
    	return self.name

class AboutContentBlock(models.Model):
    TOP = 'T'
    BOTTOM = 'B'
    POSITIONS = ((TOP, 'top'), (BOTTOM, 'bottom'))
    title = models.CharField(max_length=100, null=False, blank=False,
							help_text="Content Block Title")
    content = HTMLField()
    display = models.BooleanField()
    position = models.CharField(max_length=1, choices=POSITIONS)

    def __unicode__(self):
        return self.title

class Career(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, help_text="Career Name")
    description = HTMLField()

    def __unicode__(self):
        return self.name

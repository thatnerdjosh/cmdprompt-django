from django.db import models

class Quote(models.Model):
	approved = models.BooleanField(null=False, default=False)
	quote = models.TextField(null=False, blank=False)
	who = models.CharField(max_length=100, null=False, blank=False)
	org = models.CharField(max_length=100, null=False, blank=False)
	link = models.URLField(null=False, blank=False)
	feature = models.BooleanField(null=False, default=False, help_text="Display on home page, only one quote can be displayed at a time")

	def __unicode__(self):
		if len(self.quote) > 75:
			return "%s..." % self.quote[:75]
		else:
			return self.quote

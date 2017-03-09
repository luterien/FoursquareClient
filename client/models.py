from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


class Search(models.Model):

	query = models.CharField(max_length=100, 
		null=True, blank=True)
	location = models.CharField(max_length=150, 
		null=True, blank=True)
	date_created = models.DateTimeField(
		default=timezone.now)

	class Meta:
		ordering = ("-date_created",)

	def __unicode__(self):
		return u"%s - %s" % (self.query, self.location)


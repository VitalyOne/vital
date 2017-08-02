from django.db import models
from django.utils import timezone


class Detal(models.Model):
    
	catalog_number = models.CharField(max_length=250, unique=True)
	alternativ_number = models.CharField(max_length=250, unique=True)
	opisanie = models.TextField()
	kolvo_zaprosov = models.IntegerField(default=0)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey('auth.User')

    

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.catalog_number
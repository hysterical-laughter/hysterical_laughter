from django.db import models

from django.utils import timezone
class picture(models.Model):
	# file will be uploaded to MEDIA_ROOT/uploads
	picture = models.FileField(upload_to='funny_images/')
	description	= models.CharField(max_length=300, default=None)
	date		= models.DateTimeField(default=timezone.now)
	def __str__(self):
		return str(self.picture)

class like(models.Model):
	picture = models.CharField(max_length=500)
	likes   = models.CharField(max_length=10000)
	def __str__(self):
		return str(self.picture)

class comment(models.Model):
	username = models.CharField(max_length=100)
	picture  = models.CharField(max_length=500)
	comment  = models.CharField(max_length=1000)
	date     = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return str(self.picture)

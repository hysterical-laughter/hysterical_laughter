from django.db import models
from django.utils import timezone
class video(models.Model):
	video		= models.CharField(max_length=300)
	description	= models.CharField(max_length=300)
	date		= models.DateTimeField(default=timezone.now)
	def __str__(self):
		return str(self.description)

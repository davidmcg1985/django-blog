from django.db import models
from django.utils import timezone


class Post(models.Model): # Django model called Post (it is an object)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self): # Django method (lowercase and underscores)
		self.published_date = timezone.now()
		self.save()

	def __str__(self): # This Django method returns something
		return self.title

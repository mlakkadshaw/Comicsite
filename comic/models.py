from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Comic(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200, null=True, blank=True)
	comic_image = models.ImageField(upload_to="images/")
	authors = models.ManyToManyField(Author)

	def __unicode__(self):
		return self.name

from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField(max_length=500, null=True, blank=True)

	class meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contact"

	def __str__(self):
		return self.name
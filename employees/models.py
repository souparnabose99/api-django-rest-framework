from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=200)
	age = models.CharField(max_length=200)
	domain = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	interest = models.CharField(max_length=200)

	def __str__(self):
		return self.name

# Create your models here.

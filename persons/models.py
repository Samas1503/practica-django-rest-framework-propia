from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_birth = models.DateTimeField(default='1-1-1999')
	created_at = models.DateTimeField(auto_now_add=True)
	dni = models.PositiveIntegerField()

class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=300)
	email = models.CharField(max_length=200)
	active = models.BooleanField(default=True)
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
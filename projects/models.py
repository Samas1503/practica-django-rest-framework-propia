from django.db import models
from persons.models import User

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	tecnology = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.name + ' - ' + self.created_by.username

class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	important = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	from_project = models.ForeignKey(Project, on_delete=models.CASCADE)
	def __str__(self):
		return self.title + ' - ' + self.from_project.name
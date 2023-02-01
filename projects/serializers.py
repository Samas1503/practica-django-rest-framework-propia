from rest_framework import serializers
from .models import Project, Task
from persons.models import Person, User

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('id','name','description','tecnology')
		read_only_fields = ('created_at','created_by')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields  = ('id','title', 'description','important')
		read_only_fields = ('created_at','created_by','from_project')
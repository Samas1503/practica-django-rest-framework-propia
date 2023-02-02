from rest_framework import serializers
from .models import Project, Task
from persons.models import Person, User

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('id','name','description','tecnology','created_by')
		read_only_fields = ('created_at',)

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields  = ('id','title', 'description','important','from_project','created_by')
		read_only_fields = ('created_at',)
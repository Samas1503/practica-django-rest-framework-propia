from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	permission_class = [permissions.AllowAny]
	serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	permission_class = [permissions.AllowAny]
	serializer_class = TaskSerializer
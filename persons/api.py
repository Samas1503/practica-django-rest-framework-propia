from .models import Person, User
from .serializers import PersonSerializer, UserSerializer
from rest_framework import viewsets, permissions

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = PersonSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = UserSerializer
from rest_framework import serializers
from .models import Person, User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','password','email','active','person')

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ('id','first_name','last_name','date_birth','dni')
		read_only_fields = ('created_at',)
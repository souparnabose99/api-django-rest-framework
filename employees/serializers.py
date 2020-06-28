from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'url', 'name', 'age', 'domain', 'role', 'interest')
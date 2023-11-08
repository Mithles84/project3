from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class meta:
        model=Employee
        fields="__all__"
    
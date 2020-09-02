from rest_framework import serializers
from . models import employees

class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'
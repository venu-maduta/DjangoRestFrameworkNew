from rest_framework import serializers
from Customer_App.models import Customer_data

class EmployeeSerializers(serializers.ModelSerializer):
    # work_exp = serializers.
    class Meta:
        model = Customer_data
        fields = ['name']

class FetchEmployeeDetails(serializers.ModelSerializer):

    class Meta:
        model = Customer_data
        # fields = ['id','name','age','gender','email']
        fields = '__all__'
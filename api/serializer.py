from rest_framework.serializers import ModelSerializer, ValidationError
from employees.models import Employee
import re

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
    def validate_email(self, value):
        if not value.endswith('@company.com'):
            raise ValidationError("Email must be a company email address.")
        return value
    
    def validate_salary(self, value):
        if value <= 0:
            raise ValidationError("Salary must be a positive number.")
        return value
    
    def validate_emp_id(self, value):
        pattern = r'^EMP\d+$'
        if not re.match(pattern, value):
            raise ValidationError("Employee ID must start with 'EMP' followed by digits. (e.g., EMP001)")
        return value
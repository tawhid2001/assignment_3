from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.emp_id})"
    
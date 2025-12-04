import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    # Use case 1: filter employees by desiganation
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='exact')
    
    # Use case 2: Name contains word
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    
    # Use case 3: filter employees by emp_id range
    emp_id_min = django_filters.CharFilter(field_name='emp_id', lookup_expr='gte')
    emp_id_max = django_filters.CharFilter(field_name='emp_id', lookup_expr='lte')
    
    # Use case 4: Salary range
    
    salary_min = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    
    class Meta:
        model = Employee
        fields = ['designation', 'name', 'emp_id_min', 'emp_id_max', 'salary_min', 'salary_max']
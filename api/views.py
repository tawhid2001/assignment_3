from django.shortcuts import render, get_object_or_404
from rest_framework import status,mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from employees.models import Employee
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EmployeeFilter


# Create your views here.

# # API view to handle Employee data
# class EmployeeView(APIView):
#     def get(self, request):
#         # Logic to retrieve and return employee data
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         # Logic to create a new employee
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return get_object_or_404(Employee, pk=pk)
#         except Employee.DoesNotExist:
#             return None
    
#     def get(self, request, pk):
#         # Logic to retrieve a specific employee by ID
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         # Logic to update a specific employee by ID
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         # Logic to delete a specific employee by ID
#         employee = self.get_object(pk)
#         if not employee:
#             return Response({"error": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # Using Generic Views and Mixins for CRUD operations
# class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
    
    
# class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)

#     def put(self, request, pk):
#         return self.update(request, pk=pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)
    
    
    
# # Using Generic Class-Based Views for CRUD operations
# class EmployeeView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
    
# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
    
# Using ViewSets for CRUD operations
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
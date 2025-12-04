from django.urls import path, include
# from .views import EmployeeView, EmployeeDetailView
from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', EmployeeViewSet)




urlpatterns = [    # Define your API endpoints here
        # path('employees/', EmployeeView.as_view(), name='employee-list'),
        # path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
        path('', include(router.urls)),
]
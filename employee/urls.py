from django.urls import path
from employee.views import *

urlpatterns = [
    path('', EmployeeList, name='employee-list'),
    path('details/<int:id>/', EmployeeDetails, name='employee-details'),
    path('edit/<int:id>/', EmployeeEdit, name='employee-edit'),
    path('add/', EmployeeAdd, name='employee-add'),
    path('delete/<int:id>/', EmployeeDelete, name='employee-delete'),


]
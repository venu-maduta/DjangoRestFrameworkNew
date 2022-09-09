from django.urls import path
from Customer_App import views
#
urlpatterns=[
    path('EmployeeCreation/',views.CreateEmployee.as_view(),name='create_records'),
    path('EmployeeUpdation/',views.UpdateEmployeeDetails.as_view(),name='update_records'),
    path('EmployeeDeletion/',views.DeleteEmployee.as_view(),name='delete_records'),
    path('EmployeeFetch/<int:pk>/',views.GetEmployeeDetails.as_view(),name='get_records'),
    path('EmployeeFetch/',views.GetEmployeeDetails.as_view(),name='get_records'),
]

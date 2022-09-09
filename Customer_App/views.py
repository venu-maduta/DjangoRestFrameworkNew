from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status, generics
from rest_framework.compat import coreapi
from rest_framework.schemas import AutoSchema
from Customer_App.models import *
from Customer_App.helper import *
from Customer_App.error_checks import *
from Customer_App.error_messages import *
from Customer_App.success_messages import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from Customer_App.serializers import *
# Create your views here.

class CreateEmployee(APIView):

    # schema = CustomSchema()

    def post(self,request, format=None):
        try:
            data = request.data
            email = data.get("email")
            error_checks = create_employee_request(data)
            if not error_checks:
                try:
                    if email:
                        check_existing_employee = Customer_data.objects.filter(email=email)
                        if not check_existing_employee.exists():
                            create_employee = requestFieldMappingWithTable(data)
                            if create_employee:
                                return Response(create_employee)
                            else:
                                return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR, EMPLOYEE_CREATION_FAILED))
                        else:
                            return Response(create_response(status.HTTP_412_PRECONDITION_FAILED, EMPLOYEE_ALREADY_EXIST))
                    return Response(create_response(status.HTTP_412_PRECONDITION_FAILED,EMPLOYEE_CREATION_FAILED))
                except Exception as e:
                    return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR, EMPLOYEE_CREATION_FAILED))
            return Response(create_response(status.HTTP_400_BAD_REQUEST,INVALID_REQUEST_BODY))
        except Exception as e:
            return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EMPLOYEE_CREATION_FAILED))

class UpdateEmployeeDetails(APIView):

    def put(self,request,format=None):

        try:
            data = request.data
            try:
                error_checks = check_update_emp_request(data)
                if not error_checks:
                    try:
                        get_emp = Customer_data.objects.get(id=data.get("regId"))
                    except Customer_data.DoesNotExist:
                        return Response(create_response(status.HTTP_412_PRECONDITION_FAILED,EMPLOYEE_DOES_NOT_EXIST))
                    if get_emp:
                        # data_parse = JSONParser().parse(request)
                        emp_serializer = EmployeeSerializers(get_emp,data=data)
                        if emp_serializer.is_valid():
                            emp_serializer.save()
                            return JsonResponse(create_response(status.HTTP_200_OK,EMPLOYEE_UPDATED_SUCCESSFULLY))
                        return JsonResponse(create_response(status.HTTP_412_PRECONDITION_FAILED,emp_serializer.errors))
                else:
                    return Response(create_response(status.HTTP_412_PRECONDITION_FAILED,INVALID_REQUEST_BODY))
            except Exception as e:
                return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EMPLOYEE_UPDATION_FAILED))
        except Exception as e:
            return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EMPLOYEE_UPDATION_FAILED))


class DeleteEmployee(APIView):

    def post(self,request,format=None):
        try:
            data = request.data
            try:
                error_checks = check_delete_request(data)
                if not error_checks:
                    reg_id = data.get("regId")
                    try:
                        delete_employee = Customer_data.objects.get(id=reg_id)
                    except:
                        return Response(create_response(status.HTTP_200_OK,EMPLOYEE_DOES_NOT_EXIST))
                    if delete_employee:
                        delete_employee.delete()
                        return Response(create_response(status.HTTP_200_OK,EMPLOYEE_DELETED_SUCCESSFULLY))
            except:
                return Response(create_response(status.HTTP_400_BAD_REQUEST,INVALID_REQUEST_BODY))
        except Exception as e:
            return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EMPLOYEE_DELETION_FAILED))


class GetEmployeeDetails(APIView):

    def get(self,request,pk=None,format=None):
        try:
            id = pk
            employee_details = None
            if id is None:
                try:
                    employee_details = Customer_data.objects.all()
                except:
                    return Response(create_response(status.HTTP_412_PRECONDITION_FAILED,EMPLOYEE_DETAILS_FETCH_FAILED))
            else:
                try:
                    employee_details = Customer_data.objects.get(id=id)
                except:
                    return Response(create_response(status.HTTP_412_PRECONDITION_FAILED,EMPLOYEE_DOES_NOT_EXIST))
            if employee_details:
                emp_serializer = None
                if id is not None:
                    emp_serializer = FetchEmployeeDetails(employee_details,many=False)
                else:
                    emp_serializer = FetchEmployeeDetails(employee_details,many=True)
                return Response({"status":status.HTTP_200_OK,
                                 "success":True,
                                 "Employees":emp_serializer.data},status.HTTP_200_OK)
        except Exception as e:
            return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EMPLOYEE_DETAILS_FETCH_FAILED))

from Customer_App.models import *
from Customer_App.error_checks import *
from Customer_App.error_messages import *
from Customer_App.success_messages import *
from rest_framework.response import Response
from rest_framework import  status

def create_response(status_code,error_body):
    try:
        return {
            "statusCode": status_code,
            "result" : error_body
        }
    except Exception as e:
        return Response(status.HTTP_412_PRECONDITION_FAILED,{"message":"Exception in create response function","success":False})

def requestFieldMappingWithTable(data):
    try:
        name, email, age, gender, phoneNo = data.get("name"), data.get("email"), data.get("age"), data.get("gender"), data.get("phoneNo")
        address_details, house_num, street, city, state = data.get("addressDetails"), data.get("addressDetails").get("hno"),data.get("addressDetails").get("street"), data.get("addressDetails").get("city"),data.get("addressDetails").get("state")
        workExperience, comp_name, from_date, toDate, address = data.get("workExperience")[0], data.get("workExperience")[0].get("companyName"),data.get("workExperience")[0].get("fromDate"), data.get("workExperience")[0].get("toDate"), data.get("workExperience")[0].get("address")
        qualification, qualification_name, qua_from_date, qua_to_date, qua_percentage = data.get("qualifications")[0], data.get("qualifications")[0].get("qualificationName"),data.get("qualifications")[0].get("fromDate"), data.get("qualifications")[0].get("toDate"),data.get("qualifications")[0].get("percentage")
        project, proj_tile, proj_desc = data.get("projects")[0], data.get("projects")[0].get("title"), data.get("projects")[0].get("description")
        photo = data.get("photo")

        createEmployee = Customer_data.objects.create(name=name,email=email,age=age,gender=gender,phone_number=phoneNo,
                                                      address_details=address_details,house_num = house_num,street=street,city=city,state=state,
                                                      workExperience=workExperience,companyName=comp_name,fromDate=from_date,toDate=toDate,address=address,
                                                      qualifications=qualification,qualificationName=qualification_name,percentage=qua_percentage,quafromDate=qua_from_date,quaToDate=qua_to_date,
                                                      projects=project,title=proj_tile,description=proj_desc,photo=photo)
        if createEmployee:
            get_employee = Customer_data.objects.get(email=email)
            if get_employee:
                success_msg = EMPLOYEE_CREATED_SUCCESSFULLY
                success_msg['regid'] = get_employee.id
                resp = create_response(status.HTTP_200_OK,success_msg)
                return resp
            else:
                return False
        else:
            return False
    except Exception as e:
        return Response(create_response(status.HTTP_500_INTERNAL_SERVER_ERROR,EXCEPTION_IN_MAPPING_REQUEST_FIELDS_CREATE_EMP))


from .helper import *
from rest_framework.response import Response
from rest_framework import  status, generics
from Customer_App.error_messages import *

def create_employee_request(data):
    name, email, age, gender, phoneNo = data.get("name"), data.get("email"), data.get("age"), data.get("gender"),data.get("phoneNo")
    address_details,house_num,street,city,state = data.get("addressDetails"), data.get("addressDetails").get("hno"),data.get("addressDetails").get("street"),data.get("addressDetails").get("city"),data.get("addressDetails").get("state")
    workExperience,comp_name,from_date,toDate,address =  data.get("workExperience"),data.get("workExperience")[0].get("companyName"),data.get("workExperience")[0].get("fromDate"),data.get("workExperience")[0].get("toDate"),data.get("workExperience")[0].get("address")
    qualification,qualification_name,qua_from_date,qua_to_date,qua_percentage = data.get("qualifications"),data.get("qualifications")[0].get("qualificationName"),data.get("qualifications")[0].get("fromDate"),data.get("qualifications")[0].get("toDate"),data.get("qualifications")[0].get("percentage")
    project,proj_tile,proj_desc = data.get("projects"),data.get("projects")[0].get("title"),data.get("projects")[0].get("description")
    photo = data.get("photo")

    if not data or None in [name, email, age, gender, phoneNo,address_details,house_num,street,city,state,
                        workExperience,comp_name,from_date,toDate,address,qualification,qualification_name,
                        qua_from_date,qua_to_date,qua_percentage,project,proj_tile,proj_desc,photo] or not len(address_details) or not len(workExperience) or not len(qualification):
        return False


def check_update_emp_request(data):
    if not data.get("regId"):
        return Response(create_response(status.HTTP_400_BAD_REQUEST,INVALID_REQUEST_BODY))
    else:
        check_other_parameters = create_employee_request(data)
        if check_other_parameters:
            return True
        else:
            return False

def check_delete_request(data):
    if not data.get("regId"):
        return Response(create_response(status.HTTP_400_BAD_REQUEST,INVALID_REQUEST_BODY))
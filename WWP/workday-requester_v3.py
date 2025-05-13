# # https://community.workday.com/sites/default/files/file-hosting/productionapi/versions/v43.2/index.html

import json
import requests
import xmltodict
from xmltodict import parse

tenant_Name = "woundedwarriorproject"
username = f"ISU_UMRA@{tenant_Name}"
password = "I9#sa@Rm4"
url = f"https://wd5-services1.myworkday.com/ccx/service/{tenant_Name}/Human_Resources/"
employee_ID = 12581

# def exportPhotoFromWorkday():
request_body = f"""<xsd:Envelope xmlns:xsd="http://schemas.xmlsoap.org/soap/envelope/">
<xsd:Header>
    <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
    <wsse:UsernameToken>
        <wsse:Username>{username}</wsse:Username>
        <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{password}</wsse:Password>
    </wsse:UsernameToken>
    </wsse:Security>
</xsd:Header>
<env:Body xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
    <wd:Get_Workers_Request xmlns:wd="urn:com.workday/bsvc" wd:version="v43.2">
    <wd:Request_References wd:Ignore_Invalid_References="true" wd:Skip_Non_Existing_Instances="true">
        <wd:Worker_Reference>
        <wd:ID wd:type="Employee_ID">{employee_ID}</wd:ID>
        </wd:Worker_Reference>
    </wd:Request_References>
    <wd:Response_Group>
        <wd:Include_Reference>true</wd:Include_Reference>

    </wd:Response_Group>
    </wd:Get_Workers_Request>
</env:Body>
</xsd:Envelope>"""
headers = {
    'Content-Type': 'text/txt; charset=utf-8'
}

response = requests.request(method="POST", url=url, headers=headers, data=request_body)
response.json
parsed_response = json.dumps(parse(response.content))

# photoInfo = json.loads(parsed_response)

# for n in photoInfo:
#     print("Name",n["Worker_Descriptor"])
#     print()

print (response.json)



# <wd:Include_Photo>true</wd:Include_Photo>

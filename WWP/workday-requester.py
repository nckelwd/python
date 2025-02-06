# # https://community.workday.com/sites/default/files/file-hosting/productionapi/versions/v43.2/index.html

import json
import requests
from xmltodict import parse

tenant_Name = "woundedwarriorproject"
username = f"ISU_UMRA@{tenant_Name}"
password = "I9#sa@Rm4"
url = f"https://wd5-services1.myworkday.com/ccx/service/{tenant_Name}/Human_Resources/"
# employee_ID = 12581

# def getEmployeeIDs():
body_employeeID = f"""<xsd:Envelope xmlns:xsd="http://schemas.xmlsoap.org/soap/envelope/">
<xsd:Header>
  <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
    <wsse:UsernameToken>
      <wsse:Username>{username}</wsse:Username>
      <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{password}</wsse:Password>
    </wsse:UsernameToken>
  </wsse:Security>
</xsd:Header>
<env:Body xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
  <bsvc:Get_Workers_Request bsvc:version="v43.2" xmlns:bsvc="urn:com.workday/bsvc">
    <bsvc:Response_Group>
      <bsvc:Include_Personal_Information>true</bsvc:Include_Personal_Information>
    </bsvc:Response_Group>
  </bsvc:Get_Workers_Request>
</env:Body>
</xsd:Envelope>"""
headers_employeeID = {
    'Content-Type': 'text/xml; charset=utf-8'
}
response_employeeID = requests.request(method="POST", url=url, headers=headers_employeeID, data=body_employeeID)
parsedResponse_employeeID = json.dumps(parse(response_employeeID.content))

print (parsedResponse_employeeID["wd:Worker_ID"])

# def exportPhotoFromWorkday():
#   request_body = f"""<xsd:Envelope xmlns:xsd="http://schemas.xmlsoap.org/soap/envelope/">
#     <xsd:Header>
#       <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
#         <wsse:UsernameToken>
#           <wsse:Username>{username}</wsse:Username>
#           <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{password}</wsse:Password>
#         </wsse:UsernameToken>
#       </wsse:Security>
#     </xsd:Header>
#     <env:Body xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
#       <wd:Get_Workers_Request xmlns:wd="urn:com.workday/bsvc" wd:version="v43.2">
#         <wd:Request_References wd:Ignore_Invalid_References="true" wd:Skip_Non_Existing_Instances="true">
#           <wd:Worker_Reference>
#             <wd:ID wd:type="Employee_ID">{employee_ID}</wd:ID>
#           </wd:Worker_Reference>
#         </wd:Request_References>
#         <wd:Response_Group>
#           <wd:Include_Reference>true</wd:Include_Reference>
#           <wd:Include_Photo>true</wd:Include_Photo>
#         </wd:Response_Group>
#       </wd:Get_Workers_Request>
#     </env:Body>
#   </xsd:Envelope>"""
#   headers = {
#       'Content-Type': 'text/xml; charset=utf-8'
#   }
#   response = requests.request(method="POST", url=url, headers=headers, data=request_body)
#   parsed_response = json.dumps(parse(response.content))
#   print (parsed_response)

# exportPhotoFromWorkday()

# Get_Workers_Request.Response_Group.Include_Photo = true;
# workerType.Worker_Data.Worker_ID

# if (workerType.Worker_Data.Photo_Data != null & Microsoft.VisualBasic.CompilerServices.Operators.CompareString(this.PhotoPath, "", false) != 0)
#           {
#             row.Photo_FileName = workerType.Worker_Data.Photo_Data.Filename;
#             if (row.Photo_FileName.Length > 0 & row.Photo_FileName.Contains("."))
#             {
#               byte[] image = workerType.Worker_Data.Photo_Data.Image;
#               System.IO.File.WriteAllBytes(this.PhotoPath + row.UserID + row.Photo_FileName.Substring(row.Photo_FileName.LastIndexOf(".")), image);
#             }
#           }
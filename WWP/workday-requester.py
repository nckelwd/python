# https://community.workday.com/sites/default/files/file-hosting/productionapi/versions/v43.2/index.html

import json
import requests
from xmltodict import parse

tenant_Name = "woundedwarriorproject"
username = f"ISU_UMRA"
password = "I9#sa@Rm4"
url = f"https://wd5-services1.myworkday.com/ccx/service/{tenant_Name}/Human_Resources/v21.1"
page_number = 1

request_body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:bsvc="urn:com.workday/bsvc">
   <soapenv:Header>
       <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
           <wsse:UsernameToken>
               <wsse:Username>{username}</wsse:Username>
               <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">{password}</wsse:Password>
           </wsse:UsernameToken>
       </wsse:Security>
   </soapenv:Header>
   <soapenv:Body>
       <bsvc:Employee_Photo_Data>
           <bsvc:Response_Filter>
               <bsvc:Page>{page_number}</bsvc:Page>
           </bsvc:Response_Filter>
       </bsvc:Employee_Photo_Data>
   </soapenv:Body>
</soapenv:Envelope>"""

response = requests.request(method="POST", url=url, data=request_body)

parsed_response = json.loads(parse(response.content))

import zeep
from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken

hostname = ''
tenant_name = 'woundedwarriorproject'
employee_id = '12581'
user = 'ISU_UMRA'
password = 'I9#sa@Rm4'
url = f"https://wd5-services1.myworkday.com/ccx/service/{tenant_name}/Human_Resources/v21.1"

transport = Transport(timeout=10)
client = Client(url, wsse=UsernameToken(user, password),transport=transport)

request_dict = {
    'Worker_Data': {
        'Worker_ID': {
            'type': 'string',
            '_value_1': employee_id
        },
        'Descriptor' : None
    },
    'Skip_Non_Existing_Instances': None,
    'Ignore_Invalid_References': None
}

client.service.Get_Workers(request_dict)

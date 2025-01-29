import requests

def get_access_token(client_id, client_secret):
    url = "https://workday.com/ccx/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=data)
    return response.json()["access_token"]

def make_api_request(endpoint, method="GET", data=None):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://workday.com/api/v1/{endpoint}"
    
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    # Add other methods as needed
    
    response.raise_for_status()
    return response.json()

def get_employee_info(employee_id):
    data = make_api_request(f"employees/{employee_id}")
    return {
        "name": data["name"],
        "email": data["email"],
        "department": data["department"]["name"]
    }

employee = get_employee_info("12345")
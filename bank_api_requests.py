import requests
import json
import time


# # Payment Requests
# def initiate_payment():
#     print("Initiate payment")
#     return "Success"

# def execute_payment():
#     print("Execute payment")
#     return "Success"


# # Account Balance Requests
# def check_balance():
#     print("Check balance")
#     return "Success"


# # Utility Requests
# def utility_payment():
#     print("Utility payment")
#     return "Success" 


# Global Variables 
json_file_env = "environment_variables.json"
base_url = "https://sandbox-apis.bankofcyprus.com/df-boc-org-sb/sb/psd2"
client_id = "bd230620-1aa5-4509-858c-81e902d5c7e4"
client_secret = "vD7bP6rU3uW5yT7dW7iU1wF5oX6yS5rC2mC8vF5nX0mW6sI2nG"
x_client_certificate = "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"


# TODO - MAYBE DELETE
# Load environment variables from postman export
def load_environment_variable(json_file):
    try:
        with open(json_file, 'r') as file:
            env_variables = json.load(file)

            # TODO - DELETE Print values
            # Print results
            # if env_variables:
            #     print("Configuration loaded successfully:")       
        
            #     # Access the "values" field
            #     values = env_variables.get('values', [])
            #     if values:
            #         print("Values:")
            #         for value in values:
            #             name = value.get('key', '')
            #             description = value.get('value', '')
            #             print(f"  Key: {name}")
            #             print(f"  Value: {description}")
            #             print()
            
            return env_variables
    except FileNotFoundError:
        print(f"Config file '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{json_file}'. Check the file format.")
        return None

# TODO - DELETE/COMMENT
load_environment_variable(json_file_env)

# TODO - MAYBE DELETE
def get_client_details():
    env_details = load_environment_variable(json_file_env)
    required_values = []
    if env_details:
        # Access the "values" field
        values = env_details.get('values', [])
        if values:                   
            for value in values:
                name = value.get('key', '')
                value = value.get('value', '')
                if (name == "client_id"):
                    client_id = value
                elif (name == "client_secret"):
                    client_secret = value
                elif (name == "x-client-certificate"):
                    x_client_certificate = value
                elif (name == "subscriptionId"):
                    subscription_id = value           

    # TODO - DELETE 
    print(client_id)
    print(client_secret)
    print(x_client_certificate)
    print(subscription_id)

# TODO - DELETE
#get_client_details()


#Login Request
def get_login_token(): 

    url = base_url + "/oauth2/token"

    headers = {
        'x-client-certificate': x_client_certificate,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'TS013b36ab=0179594e11a1c58401072222c9ad9f309b75441c8f2f1d61b0209dbbbe67399ed7a1bf3be1a715a9ad30590eb558209cb2a693609f79e6c2593c665a9ef9da48f32793d5d8; de2a657d1673ca26a0e0abed5da67a83=9c1ce5ce174ef0e9f76b2c67b708705b'
    } 
    
    payload = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials&scope=TPPOAuth2Security'

    response = requests.request("POST", url, headers=headers, data=payload)

    # TODO - DELETE/COMMENT
    # if response.status_code == 200:
    #     # Request was successful, print the response content
    #     print("Response:")
    #     print(response.json()) 
    # else:
    #     # Request failed, print the error message
    #     print(f"Request failed with status code {response.status_code}:")
    #     print(response.text)

    k = response.json()
    access_token = k["access_token"]
    return access_token    

#get_login_token()

# WORKING
def get_account_details(account_num):

    token = get_login_token()

    url = base_url + "/v1/accounts/" + account_num

    payload = {}

    current_timestamp = int(time.time())
    current_timestamp_string = str(current_timestamp)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
        'subscriptionId': 'Subid000001-1696675553738',
        'originUserId': '50520222',
        'journeyId': '1bffa972-dc7a-4cbf-94f0-bd212c595b35',
        'timeStamp': current_timestamp_string,
        'x-client-certificate': x_client_certificate,
        'Cookie': 'TS013b36ab=0179594e117b8f1775af752203cbf7be34bc67f0873e88a4573d0574817de7a191be31f1640d731cb05782316a2ac4dacc6a6f4387cdb10c0cb6c58ce778a72c29d08bd044; de2a657d1673ca26a0e0abed5da67a83=9c1ce5ce174ef0e9f76b2c67b708705b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


get_account_details("351092345676")
import requests
import json


def load_environment_variable(json_file):
    try:
        with open(json_file, 'r') as file:
            env_variables = json.load(file)
            return env_variables
    except FileNotFoundError:
        print(f"Config file '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{json_file}'. Check the file format.")
        return None


# Login Request
def login():
    print("Log in")
    return "Success"


# Payment Requests
def initiate_payment():
    print("Initiate payment")
    return "Success"

def execute_payment():
    print("Execute payment")
    return "Success"


# Account Balance Requests
def check_balance():
    print("Check balance")
    return "Success"


# Utility Requests
def utility_payment():
    print("Utility payment")
    return "Success" 
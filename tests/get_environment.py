import requests
import json
import os

api_url = 'https://api.environments.bunnyshell.com/api'
project_id = os.getenv('BUNNYSHELL_PROJECT_ID')
auth_token = os.getenv('AUTH_TOKEN')
ephemeral_environment = os.getenv('EPHEMERAL_ENVIRONMENT')

def get_environment_id():

    url = '{}/projects/{}/environments'.format(api_url, project_id)

    api_call_headers = {'Authorization': 'Bearer ' + auth_token, 'Accept-Encoding': 'gzip, deflate, br', 'Accept': 'application/json'}

    print(api_call_headers)

    response = requests.get(url, headers=api_call_headers)
    response = response.json()

    enviroment_id = None

    for environment_info in response:
        if environment_info['name'] == ephemeral_environment:
            return environment_info['id']


def get_application_info(environment_id):

    url = '{}/projects/{}/environments/{}/applications'.format(api_url, project_id, environment_id)

    api_call_headers = {'Authorization': 'Bearer ' + auth_token, 'Accept-Encoding': 'gzip, deflate, br', 'Accept': 'application/json'}

    print(api_call_headers)

    response = requests.get(url, headers=api_call_headers)
    response = response.json()

    print(response.json())

    # enviroment_id = None

    # for environment_info in response:
    #     if environment_info['name'] == ephemeral_environment:
    #         return environment_info['id']


environment_id = get_environment_id()
get_application_info(environment_id)


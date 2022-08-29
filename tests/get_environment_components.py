import requests
import json
import os
import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

api_url = 'https://api.environments.bunnyshell.com/api'
project_id = os.getenv('BUNNYSHELL_PROJECT_ID')
auth_token = os.getenv('AUTH_TOKEN')
ephemeral_environment = os.getenv('EPHEMERAL_ENVIRONMENT')
environment_components_file = 'environment_components.json'

def get_environment_id():

    url = '{}/projects/{}/environments'.format(api_url, project_id)

    api_call_headers = {'Authorization': 'Bearer ' + auth_token, 'Accept-Encoding': 'gzip, deflate, br', 'Accept': 'application/json'}

    response = requests.get(url, headers=api_call_headers)
    response = response.json()

    for environment_info in response:
        if environment_info['name'] == ephemeral_environment:
            print("Environment info")
            print(environment_info)
            environment_id = environment_info['id']
            print('----------------')
            print("New Ephemeral Environment id is {}".format(environment_id))
            print('----------------')
            return environment_id

def wait_for_environment_to_be_ready(environment_id):

    url = '{}/environments/{}'.format(api_url, environment_id)

    api_call_headers = {'Authorization': 'Bearer ' + auth_token, 'Accept-Encoding': 'gzip, deflate, br', 'Accept': 'application/json'}


    while True:

        response = requests.get(url, headers=api_call_headers)
        environment_info = response.json()
        # pp.pprint(environment_info)

        status = environment_info['status']
    
        if status == 'running':
            break

        print("Waiting for environment to be create. Status is {}".format(status))

        time.sleep(10)

def get_application_info(environment_id):

    url = '{}/environments/{}/components'.format(api_url, environment_id)

    api_call_headers = {'Authorization': 'Bearer ' + auth_token, 'Accept-Encoding': 'gzip, deflate, br', 'Accept': 'application/json'}

    response = requests.get(url, headers=api_call_headers)
    response = response.json()

    components = response['components']

    print("Environment components")
    print(response)
    print('----------------')

    applications = {}

    for component in components:
        hosts = component['hosts']
        if len(hosts) > 0:
            for host in hosts:
                applications[component['name']] = host['hostname']

    print("Application urls")
    print(applications)
    print('----------------')

    with open(environment_components_file, 'w') as f:
        json.dump(applications, f)

environment_id = get_environment_id()
wait_for_environment_to_be_ready(environment_id)
get_application_info(environment_id)


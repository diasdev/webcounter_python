import os
import requests
import json

token_url='https://api.environments.bunnyshell.com/token'
client_id = os.getenv('BUNNYSHELL_API_CLIENT_ID')
client_secret  = os.getenv('BUNNYSHELL_API_CLIENT_SECRET')
api_username = os.getenv('BUNNYSHELL_API_USER')
api_password = os.getenv('BUNNYSHELL_API_PASSWORD')

data = {'grant_type': 'password','username': api_username, 'password': api_password}

access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret))

# debug_log("Headers {}".format(access_token_response.headers))
# debug_log("Response text {}".format(access_token_response.text))

tokens = json.loads(access_token_response.text)
token = tokens['access_token']

print(token)

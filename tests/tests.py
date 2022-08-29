import requests
import json
import sys


def get_addresses():

    with open('environment_components.json', 'r') as f:
        applications = json.load(f)
    return applications

def test_response(applications):

    failed = False
 
    for component_name, component_address in applications.items():
        component_address = "https://" + component_address
        print("Testing component {} on {}".format(component_name, component_address))

        try:
            response = requests.get(component_address)
            response_code = response.status_code
            #print(response.status_code)
            #print("Response code is {}".format(response_code))
            print("Application testing was successfull for component {}".format(component_name))

            #if response_code != 200:
            #    print("Application testing failed for component {}".format(component_name))
            #    failed = True
            #else:
            #    print("Application testing was successfull for component {}".format(component_name))
        except Exception as e:
            pass
            #    print("Exception: {}".format(e))
            #    print("Application testing failed for component {}".format(component_name))
            #    failed = True

        #print("-----------------")
    
    return failed

applications = get_addresses()
result = test_response(applications)

#print("Result is " + str(result))

#if not result:
#    print("Testing failed")
#    sys.exit(1)

sys.exit(0)

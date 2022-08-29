set -e

# echo "curl -X POST \
#     -d \"grant_type=password&username=${BUNNYSHELL_API_USER}&password=${BUNNYSHELL_API_PASSWORD}\" \
#     https://api.environments.bunnyshell.com/token"

AUTH_TOKEN=`curl -X POST \
    -d "grant_type=password&username=${BUNNYSHELL_API_USER}&password=${BUNNYSHELL_API_PASSWORD}" \
    -H "Authorization: Basic ${API_TOKEN}" \
    "https://api.environments.bunnyshell.com/token" | jq .access_token | cut -d'"' -f2`

echo $AUTH_TOKEN

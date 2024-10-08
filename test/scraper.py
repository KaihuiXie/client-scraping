import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal_ecommerce',
    'url': 'https://shop1458665992398.1688.com/page/contactinfo.htm',
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('svcxkh_isFtM', 'Zaxscdvfbg~123456'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
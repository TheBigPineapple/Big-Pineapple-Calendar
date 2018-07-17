# returns a list of charity events, with name, description, url, start/end time, location

import requests
import json
import config

headers = {"Authorization": "Bearer " + config.eventbrite_personal_OAuth}

response = requests.get(
    "https://www.eventbriteapi.com/v3/users/me/owned_events/",
    headers = headers,
    verify = True,  # Verify SSL certificate
)

# hard-coded to nyc, could take location data from Google Auth in future
latitude = '40.7547656'
longitude = '-73.9852742'
charity_category_id = '111'

params = {'location.address' : 'New York, New York', 'categories' : charity_category_id}

# {
#     "resource_uri": "https://www.eventbriteapi.com/v3/categories/111/",
#     "id": "111",
#     "name": "Charity & Causes",
#     "name_localized": "Charity & Causes",
#     "short_name": "Charity & Causes",
#     "short_name_localized": "Charity & Causes"
# }

events_response = requests.get("https://www.eventbriteapi.com/v3/events/search/",
    params = params,
    headers = headers,
    verify = True,
)
print (events_response.json()['events'])
print(type(events_response.json()['events']))

return events_response.json()['events']

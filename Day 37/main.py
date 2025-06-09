import requests
import os
from datetime import datetime as dt
from datetime import timedelta

GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{os.getenv("PIXELA_USERNAME")}/graphs"
add_pixel_endpoint = f"{pixela_graph_endpoint}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}

pixela_params = {
    "token": os.getenv("PIXELA_TOKEN"),
    "username": os.getenv("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# graph_config = {
#     "id": "graph1",
#     "name": "Book Worm",
#     "unit": "Pages",
#     "type": "int",
#     "color": "ichou"
# }

# b_response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(b_response.text)

add_pixel_params = {
    # "date": f"{dt.now().strftime('%Y%m%d')}",
    "date": f"{dt(2025, 6, 7).strftime('%Y%m%d')}",
    "quantity": input("How many pages did you read today?")
}
# print(add_pixel_params["date"])

# pixel_response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
# print(pixel_response.text)

# date_to_update = f"{dt(2025, 6, 7).strftime('%Y%m%d')}"
update_pixel_endpoint = f"{add_pixel_endpoint}/{dt.now().strftime('%Y%m%d')}"

put_params = {
    "quantity": "7"
}

# update_pixel_response = requests.put(url=update_pixel_endpoint, json=put_params, headers=headers)
# print(update_pixel_response.text)

del_pixel_response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(del_pixel_response.text)


"""" Learnings
1. After you've created a user or a graph, no need to create it again. 
Proceed with posting or updating pixels (pieces of data). Use the documentation.
"""

# client.py
import http.client
import json


conn = http.client.HTTPConnection("localhost", port=9091)


conn.request("GET", "/")


response = conn.getresponse()


if response.status == 200:
    data = response.read()


    bus_info = json.loads(data)


    print("Bus Information:")
    for bus in bus_info:
        print(f"Route: {bus['route']}, Next Stop: {bus['next_stop']}, ETA: {bus['eta']}")
else:
    print("Failed to retrieve bus information")


conn.close()
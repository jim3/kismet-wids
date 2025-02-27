import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER")
port = os.getenv("PORT")
url = f"http://{server}:{port}"  # Construct the base URL
ap = "/devices/views/phydot11_accesspoints/devices.json"


# take ap data, get all related clients and probe for details
def client_map(data):
    if not data or len(data) == 0:
        print("No data received")
        return
    print("First record structure:")
    print(json.dumps(data[0], indent=4))
    # TODO: Error checking


# make a GET request to the API and get all access points
def access_points():
    api_url = f"{url}{ap}"
    response = requests.get(api_url, auth=(username, password))  # Basic Auth
    response.raise_for_status()
    return response.json()


def main():
    data = access_points()
    print(json.dumps(data, indent=4))  # debugging

    clients = client_map(data)
    if clients:
        print("\nClient map:")
        print(clients)


if __name__ == "__main__":
    main()

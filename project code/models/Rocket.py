'''
CS 5001 Final Project
Name: Rockets information
Author: Yuhao Lu
Date: 2023-12-04
This file includes the class Rockets, which is used to fetch the rockets \
information from SpaceX API.
'''

import requests


class Rockets:
    """
    Rockets class for fetching information about SpaceX rockets.

    Attributes:
    - base_url (str): Base URL for the SpaceX API endpoint for rockets.

    Methods:
    - fetch_rocket_data(rocket_id: str) -> dict or None:
      Fetch data for a specific rocket using its unique identifier.

    """
    def __init__(self):
        """
        Initialize Rockets class with the base URL for the SpaceX API endpoint\
        for rockets.
        """
        self.base_url = "https://api.spacexdata.com/v4/rockets"

    def fetch_rocket_data(self, rocket_id):
        """
        Fetch data for a specific rocket using its unique identifier.

        Parameters:
        - rocket_id (str): The unique identifier of the rocket.

        Returns:
        - dict or None: A dictionary containing rocket data if the request is \
            successful,
          or None if the request fails.
        """
        url = f"{self.base_url}/{rocket_id}"

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print("Connection error. Unable to fetch Rocket data.")
            return None

        response = requests.get(url)

        if response.status_code == 200:
            rocket_data = response.json()
            # Check for a status key in the response
            if 'status' in rocket_data and rocket_data['status'] == 'error':
                print(f"Failed to fetch Rocket data. Error message: \
                    {rocket_data['message']}")
                return None
            return rocket_data
        else:
            print(f"Failed to fetch Rocket data. Status code: \
                {response.status_code}")
            return None

'''
CS 5001 Final Project
Name: Mars Photos
Author: Yuhao Lu
Date: 2023-12-04
This file includes the class MarsPhoto, which is used to fetch the Mars photos\
from NASA API.
'''

import requests


class MarsPhoto:
    """
    MarsPhoto class for fetching photos taken by the Mars Rover.

    Attributes:
    - api_key (str): NASA API key for authentication.
    - base_url (str): Base URL for the Mars Rover Photo API.
    - images (list): List of image URLs fetched from the API.

    Methods:
    - fetch_photos(sol: int, camera: str) -> None:
      Fetch photos from the Mars Rover Photo API for a specific Sol (Martian \
    day) and camera.

    """
    def __init__(self):
        """
        Initialize MarsPhoto with the provided NASA API key.

        Parameters:
        - api_key (str): NASA API key for authentication.
        """
        api_key = 'qda9psVqtMJgs8Kd2wG8TntSXxCq9lLbarN9uJIb'
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers"
        self.images = []

    def fetch_photos(self, sol, camera):
        """
        Fetch photos from the Mars Rover Photo API for a specific Sol (Martian
        day) and camera.

        Parameters:
        - sol (int): The Sol (Martian day) for which to fetch photos.
        - camera (str): The camera used to capture the photos.

        Returns:
        - None
        """
        url = f"{self.base_url}/curiosity/photos"
        params = {"api_key": self.api_key, "sol": sol, 'camera': camera}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            photos_data = response.json().get("photos", {})
            for photo in photos_data:
                self.images.append(photo['img_src'])
            # self.images= [photo['img_src'] for photo in photos_data]
        else:
            print(f"Failed to fetch Mars photos. Status code: \
                {response.status_code}")
            return None

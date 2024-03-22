'''
CS 5001 Final Project
Name: Astronomy Picture of the Day
Author: Yuhao Lu
Date: 2023-12-04
This file includes the class ApodData, which is used to fetch the astronomy \
picture of the day from NASA API.
'''

import requests


class ApodData:
    """
    ApodData class for fetching and saving Astronomy Picture of the Day (APOD)\
    data.

    Attributes:
    - api_key (str): NASA API key for authentication.
    - base_url (str): Base URL for the APOD API.
    - image (str): URL of the fetched astronomy picture.

    Methods:
    - fetch_apod_data(date: str) -> None:
      Fetch APOD data for a specific date.

    - save_image(date: str) -> str:
      Save the fetched astronomy picture to a local file.

    """
    def __init__(self, api_key):
        """
        Initialize ApodData with the provided NASA API key.

        Parameters:
        - api_key (str): NASA API key for authentication.
        """
        api_key = 'qda9psVqtMJgs8Kd2wG8TntSXxCq9lLbarN9uJIb'
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/planetary/apod"
        self.image = None

    def fetch_apod_data(self, date):
        """
        Fetch Astronomy Picture of the Day (APOD) data for a specific date.

        Parameters:
        - date (str): The date for which to fetch APOD data.

        Returns:
        - None
        """
        params = {"api_key": self.api_key, "date": date}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            apod_data = response.json()
            self.image = apod_data['url']
            # return apod_data
        else:
            print(f"Failed to fetch APOD data. Status code: \
                {response.status_code}")
            return None

    def save_image(self, date):
        """
        Save the fetched astronomy picture to a local file.

        Parameters:
        - date (str): The date of the fetched APOD data.

        Returns:
        - str: File path of the saved image.
        """
        if self.image:
            response = requests.get(self.image)
            if response.status_code == 200:
                # Assuming the image URL is a direct link to the image file
                image_content = response.content

                # Save the image to a local file
                file_path = f"astronomy_picture_{date}.jpg"
                with open(file_path, "wb") as file:
                    file.write(image_content)

                print(f"Image saved successfully to {file_path}")
                return file_path
            else:
                print(f"Failed to download image. Status code: \
                    {response.status_code}")
        else:
            print("No image available to save.")

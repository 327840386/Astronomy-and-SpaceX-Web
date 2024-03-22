'''
CS 5001 Final Project
Name: test_mars.py
Author: Yuhao Lu
Date: 2023-12-04
This file includes the test cases for the Mars Photos.
'''

import unittest
from unittest.mock import patch
from models.MarsPhotos import MarsPhoto
import requests


class TestMarsPhoto(unittest.TestCase):

    @patch('models.MarsPhotos.requests.get')
    def test_fetch_photos_success(self, mock_get):
        mars_photo = MarsPhoto(api_key='your_api_key')
        sol = 1000
        camera = 'FHAZ'

        # Set up a mock response with a successful status code and sample photos data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'photos': [{'img_src': 'https://example.com/photo1.jpg'}, {'img_src': 'https://example.com/photo2.jpg'}]
        }

        mars_photo.fetch_photos(sol, camera)

        # Assert that the images attribute is set correctly
        self.assertEqual(mars_photo.images, ['https://example.com/photo1.jpg', 'https://example.com/photo2.jpg'])

    @patch('models.MarsPhotos.requests.get')
    def test_fetch_photos_connection_error(self, mock_get):
        mars_photo = MarsPhoto(api_key='your_api_key')
        sol = 1000
        camera = 'FHAZ'

        # Set up a mock response to simulate a connection error
        mock_get.side_effect = requests.exceptions.ConnectionError()

        try:
            mars_photo.fetch_photos(sol, camera)
        except requests.exceptions.ConnectionError:
            pass

        # Assert that the images attribute remains None
        self.assertIsNone(mars_photo.images)

    @patch('models.MarsPhotos.requests.get')
    def test_fetch_photos_bad_status_code(self, mock_get):
        mars_photo = MarsPhoto(api_key='your_api_key')
        sol = 1000
        camera = 'FHAZ'

        # Set up a mock response with a non-200 status code
        mock_get.return_value.status_code = 404

        mars_photo.fetch_photos(sol, camera)

        # Assert that the images attribute remains None
        self.assertIsNone(mars_photo.images)

    @patch('models.MarsPhotos.requests.get')
    def test_fetch_photos_bad_status(self, mock_get):
        mars_photo = MarsPhoto(api_key='your_api_key')
        sol = 1000
        camera = 'FHAZ'

        # Set up a mock response with a successful status code but a non-success status in the JSON
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'photos': [], 'status': 'error'}

        mars_photo.fetch_photos(sol, camera)

        # Assert that the images attribute remains None
        self.assertEqual(mars_photo.images, [])


if __name__ == '__main__':
    unittest.main()

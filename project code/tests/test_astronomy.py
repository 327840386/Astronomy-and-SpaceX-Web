'''
CS 5001 Final Project
Name: test_astronomy.py
Author: Yuhao Lu
Date: 2023-12-04
This file includes the test cases for the Astronomy Picture of the Day.
'''


import unittest
from unittest.mock import patch, MagicMock
from models.AstronomyPicture import ApodData 
import requests


class TestApodData(unittest.TestCase):

    @patch('models.AstronomyPicture.requests.get')
    def test_fetch_apod_data_success(self, mock_get):
        apod_data = ApodData(api_key='your_api_key')
        date = '2023-11-12'

        # Set up a mock response with a successful status code and a sample APOD data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'url': 'https://example.com/image.jpg'}

        apod_data.fetch_apod_data(date)

        # Assert that the image attribute is set correctly
        self.assertEqual(apod_data.image, 'https://example.com/image.jpg')

    @patch('models.AstronomyPicture.requests.get')
    def test_fetch_apod_data_failure(self, mock_get):
        apod_data = ApodData(api_key='your_api_key')
        date = '2023-11-12'

        # Set up a mock response with a non-200 status code
        mock_get.return_value.status_code = 404

        # Ensure that None is returned when fetch_apod_data encounters an error
        result = apod_data.fetch_apod_data(date)
        self.assertIsNone(result)

        # Assert that the image attribute remains None
        self.assertIsNone(apod_data.image)

    @patch('models.AstronomyPicture.requests.get')
    def test_fetch_apod_data_connection_error(self, mock_get):
        apod = ApodData(api_key='your_actual_api_key')

        # Set up the mock response to raise a ConnectionError
        mock_get.side_effect = requests.exceptions.ConnectionError()

        # Call the fetch_apod_data method
        try:
            apod.fetch_apod_data(date='2023-01-01')
        except requests.exceptions.ConnectionError:
            pass

        # Assert that the image attribute is None in case of a connection error
        self.assertIsNone(apod.image)

    @patch('models.AstronomyPicture.requests.get')
    def test_fetch_apod_data_bad_status_code(self, mock_get):
        apod = ApodData(api_key='your_actual_api_key')

        # Set up the mock response for a non-200 status code
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Call the fetch_apod_data method
        apod.fetch_apod_data(date='2023-01-01')

        # Assert that the image attribute is None for a non-200 status code
        self.assertIsNone(apod.image)

    @patch('models.AstronomyPicture.requests.get')
    def test_fetch_apod_data_bad_status_message(self, mock_get):
        apod = ApodData(api_key='your_actual_api_key')

        # Set up the mock response for a successful request but with a bad status message
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'status': 'error', 'message': 'bad_message'}

        # Call the fetch_apod_data method
        apod.fetch_apod_data(date='2023-01-01')

        # Assert that the image attribute is None for a bad status message
        self.assertIsNone(apod.image)

    @patch('models.AstronomyPicture.requests.get')
    def test_save_image_success(self, mock_get):
        apod_data = ApodData(api_key='your_api_key')
        date = '2023-11-12'
        apod_data.image = 'https://example.com/image.jpg'

        # Set up a mock response for downloading the image
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'Simulated image content'

        # Use MagicMock to mock the open function and assert that it's called with the correct arguments
        with patch('builtins.open', MagicMock()) as mock_open:
            file_path = apod_data.save_image(date)

            # Assert that the open function was called with the expected arguments
            mock_open.assert_called_once_with(f"astronomy_picture_{date}.jpg", "wb")

            # Assert that the returned file path matches the expected value
            self.assertEqual(file_path, f"astronomy_picture_{date}.jpg")

    @patch('models.AstronomyPicture.requests.get')
    def test_save_image_failure(self, mock_get):
        apod_data = ApodData(api_key='your_api_key')
        date = '2023-11-12'
        apod_data.image = 'https://example.com/image.jpg'

        # Set up a mock response with a non-200 status code for downloading the image
        mock_get.return_value.status_code = 404

        # Ensure that None is returned when save_image encounters an error
        result = apod_data.save_image(date)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

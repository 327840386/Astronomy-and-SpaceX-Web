'''
CS 5001 Final Project
Name: test_rocket.py
Author: Yuhao Lu
Date: 2023-12-04
This file includes the test cases for the Rockets.
'''

import unittest
from unittest.mock import patch
from models.Rocket import Rockets
import requests


class TestRockets(unittest.TestCase):
    @patch('models.Rocket.requests.get')
    def test_fetch_rocket_data_happy_path(self, mock_get):
        rockets = Rockets()
        rocket_id = '5e9d0d95eda69974db09d1ed'

        # Set up a mock response for a successful request
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rocket_id': '5e9d0d95eda69974db09d1ed',
            'rocket_name': 'Falcon 9',
            'success': True
        }

        result = rockets.fetch_rocket_data(rocket_id)

        # Assert that the result is as expected
        expected_result = {
            'rocket_id': '5e9d0d95eda69974db09d1ed',
            'rocket_name': 'Falcon 9',
            'success': True
        }
        self.assertEqual(result, expected_result)

    @patch('models.Rocket.requests.get')
    def test_fetch_rocket_data_connection_error(self, mock_get):
        rockets = Rockets()
        rocket_id = '5e9d0d95eda69974db09d1ed'

        # Set up a mock response to simulate a ConnectionError
        mock_get.side_effect = requests.exceptions.ConnectionError()

        result = rockets.fetch_rocket_data(rocket_id)

        # Assert that the result is None due to the expected ConnectionError
        self.assertIsNone(result)

    @patch('models.Rocket.requests.get')
    def test_fetch_rocket_data_bad_status_code(self, mock_get):
        rockets = Rockets()
        rocket_id = '5e9d0d95eda69974db09d1ed'

        # Set up a mock response for a non-200 status code
        mock_get.return_value.status_code = 500

        result = rockets.fetch_rocket_data(rocket_id)

        # Assert that the result is None due to the non-200 status code
        self.assertIsNone(result)

    @patch('models.Rocket.requests.get')
    def test_fetch_rocket_data_bad_status_message(self, mock_get):
        rockets = Rockets()
        rocket_id = '5e9d0d95eda69974db09d1ed'

        # Set up a mock response with a status message indicating an error
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'status': 'error',
            'message': 'Rocket not found'
        }

        result = rockets.fetch_rocket_data(rocket_id)

        # Assert that the result is None due to the bad status message
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

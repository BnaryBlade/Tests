import requests
import unittest

class TestYandexDiskAPI(unittest.TestCase):
    base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def test_create_folder_success(self):
        headers = {'Authorization': 'мой токен скрыт'}
        params = {'path': '/test_folder'}
        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertEqual(response.status_code, 201)

        list_response = requests.get(self.base_url + '/?limit=100', headers=headers)
        self.assertIn('test_folder', [item['name'] for item in list_response.json()['items']])

    def test_create_folder_failure(self):
        headers = {'Authorization': 'мой токен скрыт'}
        params = {'path': '/test_folder'}
        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertNotEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()

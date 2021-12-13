from unittest import mock

from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from base.models import Account
from .models import CityName
from .utils import get_current_weather
from .views import CityNameViewSet
from rest_framework.test import APIRequestFactory, APIClient


class AccountAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = Account.objects.create_superuser("admin", "admin")
        self.client.force_authenticate(user=self.admin)

    def test_only_admin_can_access_endpoint(self):
        res = self.client.get('/v1/api/city_name/')
        self.assertEqual(res.status_code, 200)

        self.client.logout()

        res = self.client.get('/v1/api/account/')
        self.assertEqual(res.status_code, 403)

    def test_city_name_creation(self):
        res = self.client.post('/v1/api/city_name/', {'name': 'test'})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(CityName.objects.count(), 1)

    def test_city_name_update(self):
        CityName.objects.create(name='test')
        res = self.client.put('/v1/api/city_name/1/', {'name': 'test2'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(CityName.objects.count(), 1)
        self.assertEqual(CityName.objects.get(pk=1).name, 'test2')

    def test_city_name_delete(self):
        CityName.objects.create(name='test')
        res = self.client.delete('/v1/api/city_name/1/')
        self.assertEqual(res.status_code, 204)
        self.assertEqual(CityName.objects.count(), 0)

    def test_city_name_list(self):
        CityName.objects.create(name='test')
        res = self.client.get('/v1/api/city_name/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data['results']), 1)
        self.assertEqual(res.data['results'][0]['name'], 'test')

    @mock.patch('weather.utils')
    def test_get_current_weather_util(self, mock_utils):
        CityName.objects.create(name='Chittagong')
        mock_utils.get_current_weather.return_value = {
            "city": "Chittagong",
            "temperature": 16.02,
            "humidity": 76,
            "feels_like": 15.66
        }
        mock_utils.get_current_weather.called_once_with('Chittagong')
        self.assertEqual(mock_utils.get_current_weather.return_value, {'city': 'Chittagong',
                                                                       'temperature': 16.02, 'humidity': 76,
                                                                       'feels_like': 15.66})
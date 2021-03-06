from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from .models import Account
from .views import AccountViewSet
from rest_framework.test import APIRequestFactory, APIClient


class AccountAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin = Account.objects.create_superuser("admin", "admin")
        self.user = Account.objects.create_user("user", "user")

    def test_only_admin_can_access_endpoint(self):
        self.client.force_authenticate(user=self.admin)
        res = self.client.get('/v1/api/account/')
        self.assertEqual(res.status_code, 200)

        self.client.logout()

        res = self.client.get('/v1/api/account/')
        self.assertEqual(res.status_code, 403)

    def test_account_list(self):
        self.client.force_authenticate(user=self.admin)
        res = self.client.get('/v1/api/account/')
        response = res.json()
        self.assertEqual(response['count'], 2)

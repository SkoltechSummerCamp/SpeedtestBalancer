from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AcquireServiceTestCase(APITestCase):
    def test_cant_acquire_service(self):
        response = self.client.post(
            path=reverse('service-acquirement'),
            data={},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

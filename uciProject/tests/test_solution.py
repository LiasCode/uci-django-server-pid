from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure the response status code is 200 for good request format.
        """
        url = "/solution/"
        data = {
          "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
            {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
            {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
          ],
          "criterion": "completed"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

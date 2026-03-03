
from django.test import TestCase

from PaymentApp.models import OrderModel


class OrderModelTests(TestCase):
    def test_order_model_fields(self):
        model_fields = OrderModel._meta.get_fields()
        fields = [field.name for field in model_fields]
        expected_fields = [
            'id', 'order_id', 'product', 'email', 'merchant_id', 'phone', 'commission', 'status'
        ]
        self.assertEqual(fields, expected_fields)

    def test_status_choices(self):
        STATUS_CHOICES = (
            (1, "Не оплачено"),
            (2, "Оплачено"),
        )
        self.assertEqual(OrderModel.STATUS_CHOICES, STATUS_CHOICES)

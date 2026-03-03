
from django.test import TestCase

from services.freekassa_pay import FreeKassaSignature, FreeKassa
from services.gen_int_seq import generate_integer_sequence


class GenerateIntegerSequenceTests(TestCase):
    def test_len_gen_int_sequence(self):
        s = generate_integer_sequence(9)
        self.assertEqual(len(s), 9)

    def test_gen_int_sequence(self):
        SEQUENCE = "1234567890"
        s = generate_integer_sequence(9)
        is_other_chars = False
        for c in s:
            if c not in SEQUENCE:
                is_other_chars = True

        self.assertEqual(is_other_chars, False)


class FreeKassaSignatureTests(TestCase):
    def test_get_signature(self):
        fks = FreeKassaSignature()
        msg = "attr1:attr2:attr3:attr4"
        signature = fks.get_signature(msg)
        self.assertEqual(signature, "3bce1ee7db0c52ab7299a5580214cfa1")


class FreeKassaTests(TestCase):
    def test_get_payment_link(self):
        fk = FreeKassa(secret_word="secret_work", shop_id=12345)
        link = fk.get_payment_link(
            amount=10.12,
            order_id=123456679,
            currency="EN",
            lang="en",
            phone="79639472147",
            email="user@mail.ru",
        )
        expected_link = "https://pay.freekassa.net/?m=12345&oa=10.12&o=123456679&s=0b82be7b80b90bcdbbd432d2960099b1&currency=EN&lang=en&phone=79639472147&em=user@mail.ru"
        self.assertEqual(link, expected_link)

    def test_get_payment_link_min_param(self):
        fk = FreeKassa(secret_word="secret_work", shop_id=12345)
        link = fk.get_payment_link(
            amount=10.12,
            order_id=123456679,
        )
        expected_link = "https://pay.freekassa.net/?m=12345&oa=10.12&o=123456679&s=dbf2a510271b46312ee6a29f23bc69bb&currency=RUB&lang=ru"
        self.assertEqual(link, expected_link)

from __future__ import annotations

import hashlib


class FreeKassaSignature:

    def _get_signature(self, msg: str) -> str:
        """
        Создание сигнатуры по шаблону 'attr:attr:attr:attr'
        :param msg:
        :return: signature
        """

        return hashlib.md5(msg.encode()).hexdigest()

    def get_signature(self, msg: str) -> str:
        return self._get_signature(msg)


class FreeKassa:
    API_URL = 'https://pay.freekassa.net/'

    def __init__(self, secret_word: str, shop_id: int):
        self._secret_word = secret_word
        self._shop_id = shop_id

    def get_payment_link(
        self,
        amount: float,
        order_id: int,
        currency: str = "RUB",
        lang: str = "ru",
        phone: str | None = None,
        email: str | None = None,
        payment_system_id: int | None = None,
    ) -> str:
        """
        Создания ссылки для оплаты через freekassa
        :param amount:
        :param order_id:
        :param currency:
        :param lang:
        :param phone:
        :param email:
        :param payment_system_id:
        :return: payment link
        """

        params = []

        msg = f"{self._shop_id}:{amount}:{self._secret_word}:{currency}:{order_id}"
        fks = FreeKassaSignature()
        signature = fks.get_signature(msg)
        params.append(
            f"m={self._shop_id}&oa={amount}&o={order_id}&s={signature}&currency={currency}&lang={lang}"
        )

        if phone:
            params.append(f"phone={phone}")
        if email:
            params.append(f"em={email}")
        if payment_system_id:
            params.append(f"i={payment_system_id}")

        params_row = "&".join(params)

        return f"{self.API_URL}?{params_row}"


from django import forms
from django.conf import settings
from django.db import transaction
from phonenumber_field import phonenumber

from PaymentApp.models import OrderModel
from services.freekassa_pay import FreeKassaSign


class CallbackForm(forms.Form):
    amount = forms.FloatField()
    cur_id = forms.IntegerField()
    merchant_id = forms.IntegerField()
    merchant_order_id = forms.IntegerField()
    p_email = forms.EmailField()
    p_phone = phonenumber.PhoneNumber()
    sign = forms.CharField(max_length=70)
    commission = forms.IntegerField()
    initd = forms.IntegerField()


class CallbackForm1(forms.Form):
    AMOUNT = forms.CharField()
    CUR_ID = forms.IntegerField(required=False)
    MERCHANT_ID = forms.IntegerField()
    MERCHANT_ORDER_ID = forms.IntegerField()
    P_EMAIL = forms.EmailField(required=False)
    P_PHONE = forms.CharField(max_length=11, required=False)
    SIGN = forms.CharField(max_length=70, required=False)
    commission = forms.IntegerField(required=False)
    intid = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()

        amount = cleaned_data["AMOUNT"]

        amount_l = amount.split('.')
        if len(amount_l) > 1 and int(amount[1]) == 0:
            amount = amount_l[0]

        merchant_order_id = cleaned_data["MERCHANT_ORDER_ID"]
        form_sign = cleaned_data["SIGN"]

        fk = FreeKassaSign(
            secret_word=settings.FREEKASSA_SECRET_WORD_2, shop_id=settings.FREEKASSA_SHOP_ID
        )
        msg = f"{settings.FREEKASSA_SHOP_ID}:{amount}:{settings.FREEKASSA_SECRET_WORD_2}:{merchant_order_id}"
        sign = fk.get_signature(msg)
        if sign != form_sign:
            self.add_error("SIGN", "Signature is not valid")

    def save(self):
        amount = self.cleaned_data["AMOUNT"]
        cur_id = self.cleaned_data["CUR_ID"]
        merchant_id = self.cleaned_data["MERCHANT_ID"]
        merchant_order_id = self.cleaned_data["MERCHANT_ORDER_ID"]
        form_sign = self.cleaned_data["SIGN"]
        email = self.cleaned_data["P_EMAIL"]
        phone = self.cleaned_data["P_PHONE"]
        commission = self.cleaned_data["commission"]
        intid = self.cleaned_data["intid"]

        with transaction.atomic():
            order = OrderModel.objects.filter(order_id=merchant_order_id).first()
            if order:
                order.email = email
                order.merchant_id = merchant_id
                order.phone = phone
                order.commission = commission
                order.status = 2
                order.save()

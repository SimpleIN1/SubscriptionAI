import pprint

from django.views import View
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from PaymentApp.forms import CallbackForm, CallbackForm1
from PaymentApp.models import OrderModel
from ProductApp.models import ProductModel
from services.freekassa_pay import FreeKassa
from services.gen_int_seq import generate_integer_sequence


class PaymentRedirectView(View):

    def get(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=product_id)

        with transaction.atomic():
            order_id = generate_integer_sequence()
            fk = FreeKassa(secret_word=settings.FREEKASSA_SECRET_WORD_1, shop_id=settings.FREEKASSA_SHOP_ID)
            payment_link = fk.get_payment_link(amount=product.price, order_id=order_id)

            OrderModel.objects.create(
                order_id=order_id,
                product_id=product_id,
            )

        return redirect(payment_link)


@method_decorator(csrf_exempt, name='dispatch')
class PaymentCallbackView(View):
    form = CallbackForm1

    def post(self, request):
        # Отправка уведомления по почте типа такого
        form = self.form(request.POST)
        pprint.pprint(request.POST)
        if not form.is_valid():
            print(form.errors.as_json())
            return HttpResponse(form.errors.as_json(), content_type="application/json", status=400)

        form.save()

        return HttpResponse(
            {"status": "success"}, content_type="application/json"
        )


@method_decorator(csrf_exempt, name='dispatch')
class PaymentResultView(View):
    def get(self, request):
        print('request.GET', request.GET)
        return redirect('/')

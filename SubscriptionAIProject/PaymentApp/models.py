from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class OrderModel(models.Model):
    STATUS_CHOICES = (
        (1, "Не оплачено"),
        (2, "Оплачено"),
    )
    order_id = models.CharField(max_length=15, unique=True)
    product = models.ForeignKey("ProductApp.ProductModel", on_delete=models.PROTECT)
    email = models.EmailField(null=True, blank=True)
    merchant_id = models.CharField(max_length=150, null=True, blank=True)
    phone = PhoneNumberField(max_length=20, null=True, blank=True, default=None)
    commission = models.PositiveIntegerField(null=True, blank=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

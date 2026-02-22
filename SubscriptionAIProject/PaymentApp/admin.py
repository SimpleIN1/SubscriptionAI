from django.contrib import admin

from PaymentApp import models


# Register your models here.


@admin.register(models.OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        "id", "product", "merchant_id",  "status", "email", "phone", "commission",
    )

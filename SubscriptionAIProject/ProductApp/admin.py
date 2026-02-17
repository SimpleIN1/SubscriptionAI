from django.contrib import admin
from ProductApp import models


@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "term", "badge", )

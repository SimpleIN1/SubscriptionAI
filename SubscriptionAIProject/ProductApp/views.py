from django.views import View
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404

from ProductApp.models import ProductModel


class ProductView(View):
    template_name = "product/item.html"

    def get(self, request, product_id, *args, **kwargs):
        context = {}
        product = get_object_or_404(ProductModel, pk=product_id)
        context["product"] = product
        return render(request, self.template_name, context=context)


class ProductsView(View):
    template_name = "product/items.html"

    def get(self, request, *args, **kwargs):
        context = {}

        # caching
        products = cache.get(settings.CACHE_PRODUCTS_KEY)
        if not products:
            products = ProductModel.items()
            cache.set(settings.CACHE_PRODUCTS_KEY, products, 60*60*12)

        context["products"] = products
        return render(request, self.template_name, context=context)

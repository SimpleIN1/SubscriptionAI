from django.views import View
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
        products = ProductModel.objects.all()
        context["products"] = products
        return render(request, self.template_name, context=context)

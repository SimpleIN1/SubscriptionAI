from django.urls import path

from ProductApp import views


urlpatterns = [
    path("", views.ProductsView.as_view(), name="products"),
    path("product/<int:product_id>", views.ProductView.as_view(), name="product")
]

from django.urls import path
from PaymentApp import views

urlpatterns = [
    path('redirect/<int:product_id>', views.PaymentRedirectView.as_view(), name='payment-redirect'),
    path('callback', views.PaymentCallbackView.as_view(), name='callback-freekassa'),
    path('result', views.PaymentResultView.as_view(), name='result-freekassa'),
]

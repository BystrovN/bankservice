from django.urls import path

from .bank.views import BankWebhookView

urlpatterns = [
    path('bank/', BankWebhookView.as_view(), name='bank-webhook'),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PaymentSerializer
from apps.payments.services import payment_webhook_processing


class BankWebhookView(APIView):
    """
    Обработка вебхуков от банка:
        - Запрос изменения баланса организации.
    """

    serializer_class = PaymentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_webhook_processing(serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

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

    def post(self, request):
        # Обычно на адрес приема идет несколько типов хуков,
        # поэтому в теле основного метода была бы логика вызова разных обработчиков в зависимости от запроса.
        return self._payment_webhook(request)

    def _payment_webhook(self, request):
        """Запрос изменения баланса организации."""
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_webhook_processing(serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

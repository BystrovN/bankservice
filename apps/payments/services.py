from django.db import transaction

from apps.organizations.models import Organization
from apps.payments.models import Payment
from apps.organizations.models import BalanceLog


def payment_webhook_processing(data: dict):
    """
    Обработка данных об изменении баланса.
    Создание платежа и обновление баланса организации.
    """
    operation_id = data['operation_id']
    amount = data['amount']

    if Payment.objects.filter(operation_id=operation_id).exists():
        return

    with transaction.atomic():
        payment = Payment.objects.create(
            operation_id=operation_id,
            amount=amount,
            organization=Organization.objects.get(inn=data['payer_inn']),
            document_number=data['document_number'],
            document_date=data['document_date'],
        )

        org = payment.organization
        org.balance += amount
        org.save()

        BalanceLog.objects.create(organization=org, change_amount=amount, new_balance=org.balance)

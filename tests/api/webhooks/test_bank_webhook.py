import pytest

from apps.payments.models import Payment
from apps.organizations.models import BalanceLog


@pytest.mark.django_db
def test_new_payment_creates_payment_and_log(api_client, valid_bank_payment_data, organization):
    response = api_client.post('/api/webhook/bank/', valid_bank_payment_data, format='json')
    assert response.status_code == 200

    organization.refresh_from_db()
    assert str(organization.balance) == valid_bank_payment_data['amount']
    assert Payment.objects.filter(operation_id=valid_bank_payment_data['operation_id']).exists()
    assert BalanceLog.objects.filter(organization_id=organization.id).exists()


@pytest.mark.django_db
def test_duplicate_payment_does_nothing(api_client, valid_bank_payment_data, organization):
    api_client.post('/api/webhook/bank/', valid_bank_payment_data, format='json')
    assert BalanceLog.objects.count() == 1

    organization.refresh_from_db()
    balance_after_first_request = organization.balance

    response = api_client.post('/api/webhook/bank/', valid_bank_payment_data, format='json')
    assert response.status_code == 200

    organization.refresh_from_db()
    assert organization.balance == balance_after_first_request
    assert BalanceLog.objects.count() == 1


@pytest.mark.django_db
def test_invalid_inn_returns_error(api_client, invalid_bank_payment_data):
    response = api_client.post('/api/webhook/bank/', invalid_bank_payment_data, format='json')
    assert response.status_code == 400

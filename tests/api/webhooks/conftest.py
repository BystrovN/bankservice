import uuid

import pytest


@pytest.fixture
def valid_bank_payment_data(organization):
    return {
        'operation_id': str(uuid.uuid4()),
        'amount': '1500.00',
        'document_number': '123',
        'document_date': '2024-04-27T21:00:00Z',
        'payer_inn': organization.inn,
    }


@pytest.fixture
def invalid_bank_payment_data():
    return {
        'operation_id': str(uuid.uuid4()),
        'amount': '1500.00',
        'document_number': '123',
        'document_date': '2024-04-27T21:00:00Z',
        'payer_inn': '9999999999',
    }

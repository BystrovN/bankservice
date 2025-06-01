import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_get_balance_valid_inn(api_client, organization):
    url = reverse('organization-balance', args=[organization.inn])
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json() == {
        'inn': organization.inn,
        'balance': organization.balance,
    }


@pytest.mark.django_db
def test_get_balance_invalid_inn(api_client):
    url = reverse('organization-balance', args=['0000000000'])
    response = api_client.get(url)

    assert response.status_code == 404

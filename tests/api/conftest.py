from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from apps.organizations.models import Organization


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def organization():
    return Organization.objects.create(inn='1234567890', balance=Decimal(0))

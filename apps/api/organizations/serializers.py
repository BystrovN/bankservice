from rest_framework import serializers

from apps.organizations.models import Organization
from apps.common.constants import DECIMAL_MAX_DIGITS, DECIMAL_PLACES


class OrganizationBalanceSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(
        max_digits=DECIMAL_MAX_DIGITS, decimal_places=DECIMAL_PLACES, coerce_to_string=False
    )

    class Meta:
        model = Organization
        fields = ('inn', 'balance')

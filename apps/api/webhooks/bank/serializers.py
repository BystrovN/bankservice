from rest_framework import serializers

from apps.common.constants import INN_MAX_LENGTH
from apps.payments.models import Payment
from apps.organizations.models import Organization


class PaymentSerializer(serializers.ModelSerializer):
    operation_id = serializers.UUIDField()
    payer_inn = serializers.CharField(max_length=INN_MAX_LENGTH)

    class Meta:
        model = Payment
        fields = ('operation_id', 'amount', 'document_number', 'document_date', 'payer_inn')

    def validate_payer_inn(self, value):
        if not Organization.objects.filter(inn=value).exists():
            raise serializers.ValidationError('Organization not found.')
        return value

    def create(self, validated_data):
        inn = validated_data.pop('payer_inn')
        organization = Organization.objects.get(inn=inn)
        return Payment.objects.create(organization=organization, **validated_data)

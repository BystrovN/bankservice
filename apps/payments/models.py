from django.db import models

from apps.common.constants import DECIMAL_MAX_DIGITS, DECIMAL_PLACES
from apps.organizations.models import Organization


class Payment(models.Model):
    operation_id = models.UUIDField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=DECIMAL_MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    document_number = models.CharField(max_length=50)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment: {self.operation_id} — {self.amount}'

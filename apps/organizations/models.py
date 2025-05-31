from django.db import models

from apps.common.constants import DECIMAL_MAX_DIGITS, DECIMAL_PLACES, INN_MAX_LENGTH


class Organization(models.Model):
    inn = models.CharField(max_length=INN_MAX_LENGTH, unique=True)
    balance = models.DecimalField(max_digits=DECIMAL_MAX_DIGITS, decimal_places=DECIMAL_PLACES, default=0)

    def __str__(self):
        return f'Org: {self.inn}'


class BalanceLog(models.Model):
    """Данные об изменении баланса организации."""

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    change_amount = models.DecimalField(max_digits=DECIMAL_MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    new_balance = models.DecimalField(max_digits=DECIMAL_MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.organization.inn}: +{self.change_amount} → {self.new_balance}'

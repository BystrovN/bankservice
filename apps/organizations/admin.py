from django.contrib import admin

from .models import Organization, BalanceLog

admin.site.register([Organization, BalanceLog])

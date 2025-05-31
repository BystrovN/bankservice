from django.urls import path

from apps.api.organizations.views import OrganizationBalanceView

urlpatterns = [
    path('<str:inn>/balance/', OrganizationBalanceView.as_view(), name='organization-balance'),
]

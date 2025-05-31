from rest_framework.generics import RetrieveAPIView

from .serializers import OrganizationBalanceSerializer
from apps.organizations.models import Organization


class OrganizationBalanceView(RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationBalanceSerializer
    lookup_field = 'inn'

from rest_framework.viewsets import ModelViewSet

from warehouse.api.serializers import GuaranteeSerializer
from warehouse.models import Guarantee


class GuaranteeViewSet(ModelViewSet):
    serializer_class = GuaranteeSerializer
    queryset = Guarantee.objects.all()
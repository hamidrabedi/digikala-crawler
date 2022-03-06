from rest_framework.viewsets import ModelViewSet

from warehouse.api.serializers import PackSerializer
from warehouse.models import Pack


class PackViewSet(ModelViewSet):
    serializer_class = PackSerializer
    queryset = Pack.objects.all()
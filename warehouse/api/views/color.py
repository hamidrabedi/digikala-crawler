from rest_framework.viewsets import ModelViewSet

from warehouse.api.serializers import ColorSerializer
from warehouse.models import Color


class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
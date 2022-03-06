from rest_framework.serializers import HyperlinkedModelSerializer

from warehouse.models import Color


class ColorSerializer(HyperlinkedModelSerializer):
    
    class Meta:
            model = Color
            fields = ["title"]
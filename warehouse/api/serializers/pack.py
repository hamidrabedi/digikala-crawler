from rest_framework.serializers import HyperlinkedModelSerializer

from warehouse.models import Pack


class PackSerializer(HyperlinkedModelSerializer):
    
    class Meta:
            model = Pack
            fields = [
                "price",
                "product",
                "guarantee",
                "color",
            ]
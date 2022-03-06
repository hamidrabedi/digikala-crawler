from rest_framework.serializers import HyperlinkedModelSerializer

from warehouse.models import Product


class ProductSerializer(HyperlinkedModelSerializer):
    
    class Meta:
            model = Product
            fields = [
                "title",
                "subtitle",
                "description",
                "rating",
                "packs"
            ]
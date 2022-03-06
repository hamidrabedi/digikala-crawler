from rest_framework.viewsets import ModelViewSet

from warehouse.api.serializers import ProductSerializer
from warehouse.models import Product


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
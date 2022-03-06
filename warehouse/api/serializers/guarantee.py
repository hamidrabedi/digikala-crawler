from rest_framework.serializers import HyperlinkedModelSerializer

from warehouse.models import Guarantee


class GuaranteeSerializer(HyperlinkedModelSerializer):
    
    class Meta:
            model = Guarantee
            fields = ["title"]
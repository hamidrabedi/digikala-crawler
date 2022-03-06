from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from warehouse.utils.digikala_crawler import GetProducts
from warehouse.utils.digikala_crawler import validate_url


class CategoryView(APIView):

    def post(self, request):
        if request.data.get('category'):
            validate_url(url = request.data['category'])
            try:
                if request.data.get('pages'):
                    GetProducts(url = request.data['category'], pages = int(request.data['pages']))
                else:
                    GetProducts(url = request.data['category'], pages = 5)
            except:
                raise APIException('Category or Pages data is not valid!')

        else:
            raise APIException('No Category is given!')
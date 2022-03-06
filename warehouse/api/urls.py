from django.urls import (
    path, 
    re_path,
    include
)

from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from warehouse.api.views import(
    ProductViewSet,
    ColorViewSet,
    PackViewSet,
    GuaranteeViewSet,
    CategoryView
)

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'packs', PackViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'guarantees', GuaranteeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Digikala Crawler",
        default_version="V1",
        description="API documentation for project",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('category/',CategoryView.as_view()),
    
    #for documentation
    re_path(r'^doc/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]


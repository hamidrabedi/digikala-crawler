from django.urls import (
    path, 
    include
)

from rest_framework import routers

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

urlpatterns = [
    path('', include(router.urls)),
    path('category/',CategoryView.as_view() )
]
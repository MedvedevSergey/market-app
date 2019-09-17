from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls

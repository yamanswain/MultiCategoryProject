from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewAPI)
router.register(r'category', CategoryViewAPI)

urlpatterns = router.urls
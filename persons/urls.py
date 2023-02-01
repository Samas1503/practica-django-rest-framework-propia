from rest_framework import routers
from .api import PersonViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('api/persons',PersonViewSet,'persons')
router.register('api/users',UserViewSet,'users')

urlpatterns = router.urls
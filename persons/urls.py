from rest_framework import routers
from .api import PersonViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('persons/api',PersonViewSet,'persons')
router.register('users/api',UserViewSet,'users')

urlpatterns = router.urls
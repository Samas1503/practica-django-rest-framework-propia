from rest_framework import routers
from .api import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()

router.register('projects/api', ProjectViewSet,'projects')
router.register('tasks/api',TaskViewSet,'tasks')

urlpatterns = router.urls
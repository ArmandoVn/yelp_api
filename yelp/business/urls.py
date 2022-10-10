from rest_framework.routers import DefaultRouter

from .views import BusinessViewSet

router = DefaultRouter()
router.register(r"", BusinessViewSet, basename="business")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls

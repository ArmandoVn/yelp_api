from rest_framework.routers import DefaultRouter

from .views import YelpUserViewSet

router = DefaultRouter()
router.register(r'', YelpUserViewSet, basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
from rest_framework import routers

from apps.cars.views import CarViewSet

app_name = 'cars'

router = routers.SimpleRouter()
router.register(r'', CarViewSet)

urlpatterns = [

] + router.urls

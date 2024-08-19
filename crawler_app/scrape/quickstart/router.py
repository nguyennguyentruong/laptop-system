from django.conf import settings
from django.urls import include, re_path as url
from rest_framework import routers
from quickstart.views import CheckStatus

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"checkstatus", CheckStatus, basename="checkstatus")

urlpatterns = [
    url(r"^", include(router.urls)),
]
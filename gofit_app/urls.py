# import djoser.views
from django.conf.urls import url
from django.contrib.auth import get_user_model
from rest_framework import routers
from django.urls import path, include

from gofit_app.views import HeartInfoViewSet, SleepInfoViewSet, MotionInfoViewSet, WoHeartInfoViewSet

router = routers.DefaultRouter()
User = get_user_model()

router.register(r'heart-info', HeartInfoViewSet)
router.register(r'motion-info', MotionInfoViewSet)
router.register(r'sleep-info', SleepInfoViewSet)
router.register(r'wo-heart-info', WoHeartInfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

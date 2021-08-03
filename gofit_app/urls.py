# import djoser.views
from django.conf.urls import url
from django.contrib.auth import get_user_model
from rest_framework import routers
from django.urls import path, include

from gofit_app.views import HeartInfoViewSet, SleepInfoViewSet, MotionInfoViewSet, WoHeartInfoViewSet, \
    GetAverageMotionData, GetAverageSleepData, StepByDateViewSet, StepByDateRangeViewSet, SetSleepGoalView, \
    SleepDataByDateRangeAPI, SleepDataByDateAPI, SetStepGoalView

router = routers.DefaultRouter()
User = get_user_model()

router.register(r'heart-info', HeartInfoViewSet)
router.register(r'motion-info', MotionInfoViewSet)
router.register(r'sleep-info', SleepInfoViewSet)
router.register(r'wo-heart-info', WoHeartInfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('get-average-motion-data', GetAverageMotionData.as_view(), name='get_average_motion_data'),
    path('get-average-sleep-data', GetAverageSleepData.as_view(), name='get_average_sleep_data'),
    path('steps-by-date', StepByDateViewSet.as_view(), name='steps_by_date'),
    path('steps-by-date-range', StepByDateRangeViewSet.as_view(), name='steps_by_date_range'),
    path('sleep-time-by-date', SleepDataByDateAPI.as_view(), name='sleep_time_by_date'),
    path('sleep-time-by-date-range', SleepDataByDateRangeAPI.as_view(), name='sleep_time_by_date_range'),
    path('set-step-goal', SetStepGoalView.as_view(), name='set_step_goal'),
    path('set-sleep-goal', SetSleepGoalView.as_view(), name='set_sleep_goal'),
]

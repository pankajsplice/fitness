from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework import serializers
from .models import HeartInfo, MotionInfo, SleepInfo, WoHeartInfo
from accounts.models import UserProfile
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()


class HeartInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeartInfo
        fields = ('id', 'heart_info_dbp', 'heart_info_hr', 'heart_info_sbp', 'date_created', 'date_updated')


class MotionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotionInfo
        fields = ('id', 'motion_calorie', 'motion_data', 'motion_date', 'motion_distance', 'motion_step', 'date_created', 'date_updated')


class SleepInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SleepInfo
        fields = ('id', 'sleep_data', 'sleep_date', 'sleep_deep_time', 'sleep_light_time', 'sleep_stayup_time',
                  'sleep_total_time', 'sleep_waking_number', 'total_time', 'date_created', 'date_updated')


class WoHeartInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WoHeartInfo
        fields = ('id', 'wo_heart_data', 'wo_heart_date', 'wo_heart_day_avg', 'wo_heart_day_max', 'wo_heart_day_min',
                  'wo_heart_recent', 'wo_heart_sleep_avg', 'wo_heart_sleep_max', 'wo_heart_sleep_min', 'date_created', 'date_updated')

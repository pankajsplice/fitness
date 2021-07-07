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
        fields = "__all__"


class MotionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MotionInfo
        fields = "__all__"


class SleepInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SleepInfo
        fields = "__all__"


class WoHeartInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WoHeartInfo
        fields = "__all__"

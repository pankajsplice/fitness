from django.db import models
from utils.models import ModelMixin


class HeartInfo(ModelMixin):

    heart_info_dbp = models.CharField(max_length=100, null=True, blank=True)
    heart_info_hr = models.CharField(max_length=100, null=True, blank=True)
    heart_info_sbp = models.CharField(max_length=100, null=True, blank=True)


class MotionInfo(ModelMixin):

    motion_calorie = models.CharField(max_length=100, null=True, blank=True)
    motion_data = models.CharField(max_length=100, null=True, blank=True)
    motion_date = models.DateField(null=True, blank=True)
    motion_distance = models.CharField(max_length=100, null=True, blank=True)
    motion_step = models.CharField(max_length=100, null=True, blank=True)


class SleepInfo(ModelMixin):

    sleep_data = models.CharField(max_length=100, null=True, blank=True)
    sleep_date = models.DateField(null=True, blank=True)
    sleep_deep_time = models.TimeField(null=True, blank=True)
    sleep_light_time = models.TimeField(null=True, blank=True)
    sleep_stayup_time = models.TimeField(null=True, blank=True)
    sleep_total_time = models.TimeField(null=True, blank=True)
    sleep_waking_number = models.IntegerField(null=True, blank=True)
    total_time = models.CharField(max_length=100, null=True, blank=True)


class WoHeartInfo(ModelMixin):

    wo_heart_data = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_date = models.DateField(null=True, blank=True)
    wo_heart_day_avg = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_day_max = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_day_min = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_recent = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_sleep_avg = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_sleep_max = models.CharField(max_length=100, null=True, blank=True)
    wo_heart_sleep_min = models.CharField(max_length=100, null=True, blank=True)


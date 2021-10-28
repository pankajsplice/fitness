from django.db import models
from utils.models import ModelMixin


class HeartInfo(ModelMixin):
    heart_info_dbp = models.IntegerField(null=True, blank=True)
    heart_info_hr = models.IntegerField(null=True, blank=True)
    heart_info_sbp = models.IntegerField(null=True, blank=True)


class MotionInfo(ModelMixin):
    motion_calorie = models.FloatField(null=True, blank=True)
    motion_data = models.TextField(null=True, blank=True)
    motion_date = models.DateField(null=True, blank=True)
    motion_distance = models.FloatField(null=True, blank=True)
    motion_step = models.IntegerField(null=True, blank=True)


class SleepInfo(ModelMixin):
    sleep_data = models.TextField(null=True, blank=True)
    sleep_date = models.DateField(null=True, blank=True)
    sleep_deep_time = models.TimeField(null=True, blank=True)
    sleep_light_time = models.TimeField(null=True, blank=True)
    sleep_stayup_time = models.TimeField(null=True, blank=True)
    sleep_total_time = models.TimeField(null=True, blank=True)
    avg_heart_rate = models.PositiveIntegerField(default=0, null=True, blank=True)
    sleep_waking_number = models.IntegerField(null=True, blank=True)
    total_time = models.TimeField(max_length=100, null=True, blank=True)


class SleepDataInfo(ModelMixin):
    sleep_data = models.TextField(null=True, blank=True)
    sleep_date = models.DateField(null=True, blank=True)


class WoHeartInfo(ModelMixin):
    wo_heart_data = models.TextField(null=True, blank=True)
    wo_heart_date = models.DateField(null=True, blank=True)


class Feedback(ModelMixin):
    message = models.TextField(null=True)
    email = models.EmailField(null=True, blank=True)

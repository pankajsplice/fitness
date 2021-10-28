from django.contrib import admin
from django.contrib.admin import ModelAdmin
from gofit_app.models import WoHeartInfo, SleepInfo, MotionInfo, HeartInfo, SleepDataInfo


class HeartInfoAdmin(ModelAdmin):
    list_display = ["id", "heart_info_dbp", "heart_info_hr", "heart_info_sbp", "date_created", "date_updated"]

class MotionInfoAdmin(ModelAdmin):
    list_display = ["id", "motion_calorie", "motion_data", "motion_date", "motion_distance", "motion_step", "date_created", "date_updated"]

class SleepInfoAdmin(ModelAdmin):
    list_display = ["id", "sleep_data", "sleep_date", "sleep_deep_time", "sleep_light_time", "sleep_stayup_time",
                    "sleep_total_time", "sleep_waking_number", "total_time", "date_created", "date_updated"]

class WoHeartInfoAdmin(ModelAdmin):
    list_display = ["id", "wo_heart_data", "wo_heart_date", "date_created", "date_updated"]

class SleepDataInfoAdmin(ModelAdmin):
    list_display = ["id", "sleep_date", "sleep_data", "date_created", "date_updated"]

admin.site.register(HeartInfo, HeartInfoAdmin)
admin.site.register(MotionInfo, MotionInfoAdmin)
admin.site.register(SleepInfo, SleepInfoAdmin)
admin.site.register(WoHeartInfo, WoHeartInfoAdmin)
admin.site.register(SleepDataInfo, SleepDataInfoAdmin)

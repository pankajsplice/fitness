from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime,timedelta
from django.db.models import Avg, Min, Max
from gofit_app.models import HeartInfo, MotionInfo, SleepInfo, WoHeartInfo
from .serializers import HeartInfoSerializer, MotionInfoSerializer, SleepInfoSerializer, WoHeartInfoSerializer


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class HeartInfoViewSet(viewsets.ModelViewSet):
    queryset = HeartInfo.objects.all()
    serializer_class = HeartInfoSerializer


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class MotionInfoViewSet(viewsets.ModelViewSet):
    queryset = MotionInfo.objects.all()
    serializer_class = MotionInfoSerializer


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class SleepInfoViewSet(viewsets.ModelViewSet):
    queryset = SleepInfo.objects.all()
    serializer_class = SleepInfoSerializer


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class WoHeartInfoViewSet(viewsets.ModelViewSet):
    queryset = WoHeartInfo.objects.all()
    serializer_class = WoHeartInfoSerializer


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class GetAverageMotionData(APIView):

    def get(self, request, *args, **kwargs):
        motion_calorie_avg = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_calorie').aggregate(Avg('motion_calorie'))
        motion_calorie_min = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_calorie').aggregate(Min('motion_calorie'))
        motion_calorie_max = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_calorie').aggregate(Max('motion_calorie'))
        motion_distance_avg = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_distance').aggregate(Avg('motion_distance'))
        motion_distance_min = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_distance').aggregate(Min('motion_distance'))
        motion_distance_max = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_distance').aggregate(Max('motion_distance'))
        motion_step_avg = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_step').aggregate(Avg('motion_step'))
        motion_step_min = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_step').aggregate(Min('motion_step'))
        motion_step_max = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_step').aggregate(Max('motion_step'))
        return Response({"motion_calorie_avg": motion_calorie_avg.get('motion_calorie__avg'),
                         "motion_calorie_min": motion_calorie_min.get('motion_calorie__min'),
                         "motion_calorie_max": motion_calorie_max.get('motion_calorie__max'),
                         "motion_distance_avg": motion_distance_avg.get('motion_distance__avg'),
                         "motion_distance_min": motion_distance_min.get('motion_distance__min'),
                         "motion_distance_max": motion_distance_max.get('motion_distance__max'),
                         "motion_step_avg": motion_step_avg.get('motion_step__avg'),
                         "motion_step_min": motion_step_min.get('motion_step__min'),
                         "motion_step_max": motion_step_max.get('motion_step__max'), })


@permission_classes((AllowAny,))
@method_decorator(csrf_exempt, name='dispatch')
class GetAverageSleepData(APIView):

    def get(self, request, *args, **kwargs):
        sleep_data_avg = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_data').aggregate(Avg('sleep_data'))
        sleep_data_min = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_data').aggregate(Min('sleep_data'))
        sleep_data_max = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_data').aggregate(Max('sleep_data'))
        sleep_total_time_avg = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('total_time').aggregate(Avg('total_time'))
        sleep_total_time_min = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('total_time').aggregate(Min('total_time'))
        sleep_total_time_max = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('total_time').aggregate(Max('total_time'))
        sleep_waking_number_avg = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_waking_number').aggregate(Avg('sleep_waking_number'))
        sleep_waking_number_min = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_waking_number').aggregate(Min('sleep_waking_number'))
        sleep_waking_number_max = SleepInfo.objects.filter(sleep_date__gte=datetime.now()-timedelta(days=7)).values('sleep_waking_number').aggregate(Max('sleep_waking_number'))
        return Response({"sleep_data_avg": sleep_data_avg.get('sleep_data__avg'),
                         "sleep_data_min": sleep_data_min.get('sleep_data__min'),
                         "sleep_data_max": sleep_data_max.get('sleep_data__max'),
                         "sleep_total_time_avg": sleep_total_time_avg.get('total_time__avg'),
                         "sleep_total_time_min": sleep_total_time_min.get('total_time__min'),
                         "sleep_total_time_max": sleep_total_time_max.get('total_time__max'),
                         "sleep_waking_number_avg": sleep_waking_number_avg.get('sleep_waking_number__avg'),
                         "sleep_waking_number_min": sleep_waking_number_min.get('sleep_waking_number__min'),
                         "sleep_waking_number_max": sleep_waking_number_max.get('sleep_waking_number__max')})

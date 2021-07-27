import datetime
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime,timedelta
from django.db.models import Avg, Min, Max, Sum
from gofit_app.models import HeartInfo, MotionInfo, SleepInfo, WoHeartInfo
from .serializers import HeartInfoSerializer, MotionInfoSerializer, SleepInfoSerializer, WoHeartInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend


@method_decorator(csrf_exempt, name='dispatch')
class HeartInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    queryset = HeartInfo.objects.all()
    serializer_class = HeartInfoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                if self.request.user.is_authenticated:
                    self.perform_create(serializer)
                    d = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    custom_data = {
                        "error": False,
                        "message": 'created successfully',
                        "status_code": status.HTTP_201_CREATED,
                        "data": serializer.data
                    }
                    return Response(custom_data)
                return Response({"message": "Login Required."})
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            print(e)
            return Response({"success": False})


@method_decorator(csrf_exempt, name='dispatch')
class MotionInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    queryset = MotionInfo.objects.all()
    serializer_class = MotionInfoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                if self.request.user.is_authenticated:
                    self.perform_create(serializer)
                    d = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    custom_data = {
                        "error": False,
                        "message": 'created successfully',
                        "status_code": status.HTTP_201_CREATED,
                        "data": serializer.data
                    }
                    return Response(custom_data)
                return Response({"message": "Login Required."})
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            print(e)
            return Response({"success": False})


@method_decorator(csrf_exempt, name='dispatch')
class SleepInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = SleepInfo.objects.all()
    serializer_class = SleepInfoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                if self.request.user.is_authenticated:
                    self.perform_create(serializer)
                    d = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    custom_data = {
                        "error": False,
                        "message": 'created successfully',
                        "status_code": status.HTTP_201_CREATED,
                        "data": serializer.data
                    }
                    return Response(custom_data)
                return Response({"message": "Login Required."})
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            print(e)
            return Response({"success": False})


@method_decorator(csrf_exempt, name='dispatch')
class WoHeartInfoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = WoHeartInfo.objects.all()
    serializer_class = WoHeartInfoSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                if self.request.user.is_authenticated:
                    self.perform_create(serializer)
                    d = serializer.save()
                    headers = self.get_success_headers(serializer.data)
                    custom_data = {
                        "error": False,
                        "message": 'created successfully',
                        "status_code": status.HTTP_201_CREATED,
                        "data": serializer.data
                    }
                    return Response(custom_data)
                return Response({"message": "Login Required."})
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            print(e)
            return Response({"success": False})


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


@method_decorator(csrf_exempt, name='dispatch')
class StepByDateViewSet(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, *args, **kwargs):
        date = self.request.GET.get("date")
        data = {}
        queryset = MotionInfo.objects.filter(motion_date=date)
        if date and queryset:
            min = MotionInfo.objects.filter(motion_date=date).values('motion_step').aggregate(Sum('motion_step'))
            data["total_steps"] = int(min.get('motion_step__sum'))
            return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        return Response({"error":True, "message":"No Data Found", "status_code":status.HTTP_400_BAD_REQUEST, "data":{}})


@method_decorator(csrf_exempt, name='dispatch')
class StepByDateRangeViewSet(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, *args, **kwargs):
        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")
        day_dict = {}
        data = {}
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if from_date and to_date:
            queryset = MotionInfo.objects.filter(motion_date__gte=from_date, motion_date__lte=to_date)
            min = MotionInfo.objects.filter(motion_date__gte=from_date, motion_date__lte=to_date).values('motion_step').aggregate(Min('motion_step'))
            max = MotionInfo.objects.filter(motion_date__gte=from_date, motion_date__lte=to_date).values('motion_step').aggregate(Max('motion_step'))
            avg = MotionInfo.objects.filter(motion_date__gte=from_date, motion_date__lte=to_date).values('motion_step').aggregate(Avg('motion_step'))
            for day_name in week_list:
                if day_dict.get(day_name) == None:
                    day_dict[day_name] = 0
            for day in queryset:
                day_dict[str(day.motion_date.strftime("%A"))] = day.motion_step
            data["min_step"] = int(min.get('motion_step__min'))
            data["max_step"] = int(max.get('motion_step__max'))
            data["avg_step"] = int(avg.get('motion_step__avg'))
            data["weekly"] = day_dict
            return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        return Response({"error":True, "message":"Failed", "status_code":status.HTTP_400_BAD_REQUEST, "data":{}})

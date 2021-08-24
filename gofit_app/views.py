import datetime as dt
import time
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
from accounts.models import UserProfile
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
                    heart_info = HeartInfo.objects.filter(date_created__date=datetime.now().date()).first()
                    if heart_info:
                        heart_info.heart_info_dbp = serializer.validated_data.get('heart_info_dbp')
                        heart_info.heart_info_hr = serializer.validated_data.get('heart_info_hr')
                        heart_info.heart_info_sbp = serializer.validated_data.get('heart_info_sbp')
                        heart_info.save()
                        custom_data = {
                            "error": False,
                            "message": 'updated successfully',
                            "status_code": status.HTTP_201_CREATED,
                            "data": serializer.data
                        }
                        return Response(custom_data)
                    else:
                        self.perform_create(serializer)
                        serializer.save()
                        self.get_success_headers(serializer.data)
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
                    motion_data = MotionInfo.objects.filter(motion_date=serializer.validated_data.get('motion_date')).first()
                    if motion_data:
                        motion_data.motion_calorie = serializer.validated_data.get('motion_calorie')
                        motion_data.motion_data = serializer.validated_data.get('motion_data')
                        motion_data.motion_distance = serializer.validated_data.get('motion_distance')
                        motion_data.motion_step = serializer.validated_data.get('motion_step')
                        motion_data.save()
                        custom_data = {
                            "error": False,
                            "message": 'updated successfully',
                            "status_code": status.HTTP_201_CREATED,
                            "data": serializer.data
                        }
                        return Response(custom_data)
                    else:
                        self.perform_create(serializer)
                        serializer.save()
                        self.get_success_headers(serializer.data)
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
                    sleep_data = SleepInfo.objects.filter(sleep_date=serializer.validated_data.get('sleep_date')).first()
                    if sleep_data:
                        sleep_data.sleep_data = serializer.validated_data.get('sleep_data')
                        sleep_data.sleep_deep_time = serializer.validated_data.get('sleep_deep_time')
                        sleep_data.sleep_light_time = serializer.validated_data.get('sleep_light_time')
                        sleep_data.sleep_stayup_time = serializer.validated_data.get('sleep_stayup_time')
                        sleep_data.sleep_total_time = serializer.validated_data.get('sleep_total_time')
                        sleep_data.sleep_waking_number = serializer.validated_data.get('sleep_waking_number')
                        sleep_data.total_time = serializer.validated_data.get('total_time')
                        sleep_data.save()
                        custom_data = {
                            "error": False,
                            "message": 'updated successfully',
                            "status_code": status.HTTP_201_CREATED,
                            "data": serializer.data
                        }
                        return Response(custom_data)
                    else:
                        self.perform_create(serializer)
                        serializer.save()
                        self.get_success_headers(serializer.data)
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
            # min = MotionInfo.objects.filter(motion_date=date).values('motion_step').aggregate(Sum('motion_step'))
            steps = MotionInfo.objects.filter(motion_date=date).first()
            data["total_steps"] = int(steps.motion_step)
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
            min_steps = queryset.values('motion_step').aggregate(Min('motion_step'))
            max_steps = queryset.values('motion_step').aggregate(Max('motion_step'))
            avg_steps = queryset.values('motion_step').aggregate(Avg('motion_step'))
            data["min_step"] = min_steps.get('motion_step__min')
            data["max_step"] = max_steps.get('motion_step__max')
            data["avg_step"] = avg_steps.get('motion_step__avg')
            for day_name in week_list:
                if day_dict.get(day_name) == None:
                    day_dict[day_name] = 0
            for day in queryset:
                day_dict[str(day.motion_date.strftime("%A"))] = int(day.motion_step)
            data["weekly"] = day_dict
            return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        return Response({"error":True, "message":"Failed", "status_code":status.HTTP_400_BAD_REQUEST, "data":{}})


@method_decorator(csrf_exempt, name='dispatch')
class SetSleepGoalView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def post(self, *args, **kwargs):
        data = {}
        try:
            sleep_goal = self.request.data['sleep_goal']
            if sleep_goal:
                profile_data = UserProfile.objects.filter(user=self.request.user).first()
                profile_data.sleep_goal = sleep_goal
                profile_data.save()
                data['username'] = profile_data.user.username
                data['email'] = profile_data.user.email
                data['sleep_goal'] = profile_data.sleep_goal
                return Response({"error": False, "message": "Sleep Goal Saved", "status_code": status.HTTP_200_OK, "data": data})
            else:
                return Response({"error": True, "message": "Please Enter Sleep Goal", "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})
        except Exception as e:
            print(e)
            return Response(
                {"error": True, "message": e, "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})


@method_decorator(csrf_exempt, name='dispatch')
class SetStepGoalView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def post(self, *args, **kwargs):
        data = {}
        try:
            step_goal = self.request.data['step_goal']
            if step_goal:
                profile_data = UserProfile.objects.filter(user=self.request.user).first()
                profile_data.step_goal = step_goal
                profile_data.save()
                data['username'] = profile_data.user.username
                data['email'] = profile_data.user.email
                data['step_goal'] = profile_data.step_goal
                return Response({"error": False, "message": "Step Goal Saved", "status_code": status.HTTP_200_OK, "data": data})
            else:
                return Response({"error": True, "message": "Please Enter Step Goal", "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})
        except Exception as e:
            print(e)
            return Response(
                {"error": True, "message": e, "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})


@method_decorator(csrf_exempt, name='dispatch')
class SleepDataByDateAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, *args, **kwargs):
        date = self.request.GET.get("date")
        data = {}
        queryset = SleepInfo.objects.filter(sleep_date=date)
        if date and queryset:
            sleep_time = SleepInfo.objects.filter(sleep_date=date).latest('id')
            x = time.strptime(str(sleep_time.sleep_total_time), '%H:%M:%S')
            y = time.strptime(str(self.request.user.profile.sleep_goal), '%H:%M:%S')
            total_sleep_time_seconds = dt.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
            sleep_goal_seconds = dt.timedelta(hours=y.tm_hour, minutes=y.tm_min, seconds=y.tm_sec).total_seconds()
            sleep_time_percentage = int(total_sleep_time_seconds*100/sleep_goal_seconds)
            print(int(sleep_time_percentage))
            
            data["sleep_data"] = sleep_time.sleep_data
            data["sleep_date"] = sleep_time.sleep_date
            data["sleep_deep_time"] = sleep_time.sleep_deep_time
            data["sleep_light_time"] = sleep_time.sleep_light_time
            data["sleep_stayup_time"] = sleep_time.sleep_stayup_time
            data["sleep_total_time"] = sleep_time.sleep_total_time
            data["sleep_waking_number"] = sleep_time.sleep_waking_number
            data["total_time"] = sleep_time.total_time
            data["sleep_time_percentage"] = str(int(sleep_time_percentage))+"%"
            return Response({"error": False, "message": "Success", "status_code": status.HTTP_200_OK, "data": data})
        return Response(
            {"error": True, "message": "No Data Found", "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})


@method_decorator(csrf_exempt, name='dispatch')
class SleepDataByDateRangeAPI(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, *args, **kwargs):
        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")
        day_dict = {}
        data = {}
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if from_date and to_date:
            queryset = SleepInfo.objects.filter(sleep_date__gte=from_date, sleep_date__lte=to_date)
            for day_name in week_list:
                if day_dict.get(day_name) == None:
                    day_dict[day_name] = "00:00:00"
            for day in queryset:
                day_dict[str(day.sleep_date.strftime("%A"))] = day.sleep_total_time
            data["weekly"] = day_dict
            return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        return Response({"error":True, "message":"Failed", "status_code":status.HTTP_400_BAD_REQUEST, "data":{}})


# ----------------------------

@method_decorator(csrf_exempt, name='dispatch')
class BloodPressureDateRangeViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, *args, **kwargs):
        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")
        day_dict = {}
        data = {}
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if from_date and to_date:
            queryset = HeartInfo.objects.filter(date_created__date__gte=from_date, date_created__date__lte=to_date)
            avg_heart_info_sbp = queryset.values('heart_info_sbp').aggregate(Avg('heart_info_sbp'))
            avg_heart_info_dbp = queryset.values('heart_info_dbp').aggregate(Avg('heart_info_dbp'))
            avg_heart_info_hr = queryset.values('heart_info_hr').aggregate(Avg('heart_info_hr'))
            data["heart_info_sbp"] = avg_heart_info_sbp.get('heart_info_sbp__avg')
            data["heart_info_dbp"] = avg_heart_info_dbp.get('heart_info_dbp__avg')
            data["heart_info_hr"] = avg_heart_info_hr.get('heart_info_hr__avg')
            for day_name in week_list:
                if day_dict.get(day_name) == None:
                    day_dict[day_name] = 0
            for day in queryset:
                day_dict[str(day.date_created.strftime("%A"))] = int(day.heart_info_hr)
            data["weekly"] = day_dict
            return Response({"error": False, "message": "Success", "status_code": status.HTTP_200_OK, "data": data})
        return Response({"error": True, "message": "Failed", "status_code": status.HTTP_400_BAD_REQUEST, "data": {}})




@permission_classes((IsAuthenticated,))
@method_decorator(csrf_exempt, name='dispatch')
class GetMotionData(APIView):
    
    def get(self, request, *args, **kwargs):
        day_dict = {}
        data = {}
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        date_now = timezone.now().date()-timedelta(days=7)
        queryset = MotionInfo.objects.filter(motion_date__gte=date_now)
        date_after=date_now-timedelta(days=7)        
        queryset1 = MotionInfo.objects.filter(motion_date__gte=str(date_after), motion_date__lte=str(date_now))
        motion_calorie_avg = MotionInfo.objects.filter(motion_date__gte=timezone.now()-timedelta(days=7)).values('motion_calorie').aggregate(Avg('motion_calorie'))
        motion_calorie_sum = queryset.values('motion_calorie')
        motion_len=len(motion_calorie_sum)
        sum_mo_7=0
        for i in range(0,motion_len):
            b=motion_calorie_sum[i].get('motion_calorie')
            sum_mo_7=sum_mo_7+b
        
        motion_calorie_sum1 = queryset1.values('motion_calorie')
        motion_len1=len(motion_calorie_sum1)
        sum_mo1_after=0
        for i in range(0,motion_len1):
            b=motion_calorie_sum1[i].get('motion_calorie')
            sum_mo1_after=sum_mo1_after+b
        
        

        motion_distance_sum = queryset.values('motion_distance')
        motion_len=len(motion_distance_sum)
        sum_mo_dist_7=0
        for i in range(0,motion_len):
            b=motion_distance_sum[i].get('motion_distance')
            sum_mo_dist_7=sum_mo_dist_7+b
        
        motion_distance_sum1 = queryset1.values('motion_distance')
        motion_len1=len(motion_distance_sum1)
        sum_mo1_dist_after=0
        for i in range(0,motion_len1):
            b=motion_distance_sum1[i].get('motion_distance')
            sum_mo1_dist_after=sum_mo1_dist_after+b

        motion_step_sum = queryset.values('motion_step')
        motion_len=len(motion_step_sum)
        sum_mo_step_7=0
        for i in range(0,motion_len):
            b=motion_step_sum[i].get('motion_step')
            sum_mo_step_7=sum_mo_step_7+b
        motion_step_sum1 = queryset1.values('motion_step')
        motion_len1=len(motion_step_sum1)
        sum_mo1_step_after=0
        for i in range(0,motion_len1):
            b=motion_step_sum1[i].get('motion_step')
            sum_mo1_step_after=sum_mo1_step_after+b
        
        if sum_mo1_after > sum_mo_7:
            as1 = -((sum_mo_7-sum_mo1_after)%100)
        else:
            as1 = ((sum_mo_7-sum_mo1_after)%100)
        if sum_mo1_dist_after > sum_mo_dist_7:
            as2 = -((sum_mo_dist_7-sum_mo1_dist_after)%100)
        else:
            as2 = ((sum_mo_dist_7-sum_mo1_dist_after)%100)
        if sum_mo1_step_after > sum_mo_step_7:
            as3 = -((sum_mo_step_7-sum_mo1_step_after)%100)
        else:
            as3 = ((sum_mo_step_7-sum_mo1_step_after)%100)
        data["calorie_total"] = sum_mo_7
        
        data["calorie_percentage"] = as1
        data["distance_total"] = sum_mo_dist_7
        data["distance_percentage"] = as2
        data["step_total"] = sum_mo_step_7
        data["step_percentage"] = as3
        
        for day_name in week_list:
                if day_dict.get(day_name) == None:
                    day_dict[day_name] = 0
        for day in queryset:
            day_dict[str(day.motion_date.strftime("%A"))] = int(day.motion_step)
        data["weekly"] = day_dict
       
        return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        


@method_decorator(csrf_exempt, name='dispatch')
class StepByDateRangeHeart(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get(self, *args, **kwargs):
        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")
        to_date_con=datetime.strptime(to_date, "%Y-%m-%d").date()
        
        to_date_con=to_date_con + timedelta(days=1)
        
        day_dict = {}
        data = {}
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if from_date and to_date:         
            queryset = HeartInfo.objects.filter(date_created__gte=from_date, date_created__lte=to_date_con)
            heart_info_hr_min = queryset.values('heart_info_hr').aggregate(Min('heart_info_hr'))
            heart_info_hr_max = queryset.values('heart_info_hr').aggregate(Max('heart_info_hr'))
            heart_info_hr_avg = queryset.values('heart_info_hr').aggregate(Avg('heart_info_hr')) 
            data["heart_info_hr_min"] = heart_info_hr_min.get('heart_info_hr__min')
            data["heart_info_hr_max"] = heart_info_hr_max.get('heart_info_hr__max')
            data["heart_info_hr_avg"] = round(heart_info_hr_avg.get('heart_info_hr__avg'),2)

            return Response({"error":False, "message":"Success", "status_code":status.HTTP_200_OK, "data":data})
        return Response({"error":True, "message":"Failed", "status_code":status.HTTP_400_BAD_REQUEST, "data":{}})



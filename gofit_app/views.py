from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
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

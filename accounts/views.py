from django.views.decorators.csrf import csrf_exempt
from rest_auth.app_settings import create_token
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model, login
from accounts.serializers import OtpSerializer, PasswordResetOtpSerializer, LoginSerializer, UserSerializer, \
    RegisterSerializer, UserProfileSerializer, CustomUserSerializer, UserDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication
import random
from django.core.mail import send_mail
from go_fit.settings import DEFAULT_FROM_EMAIL, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from accounts.models import Otp, UserProfile
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_auth.views import PasswordChangeView
from rest_auth.registration.views import RegisterView

User = get_user_model()

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class RegisterAPIView(RegisterView):
    
    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        try:
            if serializer.is_valid():
                user = serializer.save(self.request)
                headers = self.get_success_headers(serializer.data)
                user_serializer = CustomUserSerializer(user)
                token, flag = Token.objects.get_or_create(user=user)
                custom_data = {
                    "error": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Registered Successfully",
                    "data": user_serializer.data,
                    "token": str(token)
                }
                return Response(custom_data, status=status.HTTP_201_CREATED)
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            error_data = {
                "error": True,
                "message": str(e),
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)


class ChangePasswordAPIView(PasswordChangeView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                custom_data = {
                    "error": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "New password has been saved.",
                    "data": serializer.data
                }
                return Response(custom_data, status=status.HTTP_201_CREATED)
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)
        except Exception as e:
            error_data = {
                "error": True,
                "message": str(e),
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)


class SendOtpApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email', '')

        if email != '':
            user = User.objects.get(email=email)
            otp = random.randint(1000, 9999)
            serializer = OtpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(otp=otp)
            subject = 'GoMove Forgot Password Otp'
            message = f"Hello {user.first_name} {user.last_name} \n Your Forgot Password Otp is {otp}"
            try:
                send_mail(subject=subject, message=message, from_email=DEFAULT_FROM_EMAIL, recipient_list=[email],
                          fail_silently=True)
            except:
                error_data = {
                    "error": True,
                    "message": 'Email not send.',
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "data": {}
                }
                return Response(error_data)
            custom_data = {
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "An otp has been sent to your email.",
                "data": {}
            }
            return Response(custom_data)
        # elif mobile != '':
        #     user = User.objects.get(email=mobile)
        #     otp = random.randint(1000, 9999)
        #     serializer = OtpSerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     serializer.save(otp=otp)
        #     title = 'LocalMingle Forgot Password Otp'
        #     body = f"Hello {user.first_name} {user.last_name} \n Your Forgot Password Otp is {otp}"
        #
        #     # Find your Account SID and Auth Token at twilio.com/console
        #     # and set the environment variables. See http://twil.io/secure
        #     account_sid = TWILIO_ACCOUNT_SID
        #     auth_token = TWILIO_AUTH_TOKEN
        #     client = Client(account_sid, auth_token)
        #     try:
        #         message = client.messages.create(body=body,
        #                                          from_='+13237451893',
        #                                          to='+91' + mobile)
        #         print(message.sid)
        #     except:
        #         return Response({'message': 'Sms not send'}, status=status.HTTP_400_BAD_REQUEST)
        #     return Response({'message': 'An otp has been sent to your mobile'}, status=status.HTTP_200_OK)
        else:
            error_data = {
                "error": True,
                "message": 'Email can not be blank.',
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)


class VerifyOtpApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email', '')
        # mobile = request.data.get('mobile', '')
        if email != '':
            otp_obj = Otp.objects.get(email=request.data['email'], verify=False)
            if otp_obj:
                if int(request.data['otp']) == otp_obj.otp:
                    serializer = OtpSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    otp_obj.verify = True
                    otp_obj.save()
                    custom_data = {
                        "error": False,
                        "status_code": status.HTTP_200_OK,
                        "message": "Your otp is verified successfully.",
                        "data": {}
                    }
                    return Response(custom_data)
                else:
                    error_data = {
                        "error": True,
                        "message": 'You have entered wrong otp.',
                        "status_code": status.HTTP_400_BAD_REQUEST,
                        "data": {}
                    }
                    return Response(error_data)
            else:
                error_data = {
                    "error": True,
                    "message": 'Please enter valid email to verify otp.',
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "data": {}
                }
                return Response(error_data)
        # elif mobile != '':
        #     otp_obj = Otp.objects.get(email=request.data['mobile'], verify=False)
        #     if otp_obj:
        #         if int(request.data['otp']) == otp_obj.otp:
        #             serializer = OtpSerializer(data=request.data)
        #             serializer.is_valid(raise_exception=True)
        #             otp_obj.verify = True
        #             otp_obj.save()
        #             return Response({'message': 'Your otp is verified successfully', 'status': status.HTTP_200_OK})
        #         else:
        #             return Response({'message': 'You have entered wrong otp.', 'status': status.HTTP_400_BAD_REQUEST})
        #     else:
        #         return Response({'message': 'Please enter valid mobile number to verify otp',
        #                          'status': status.HTTP_400_BAD_REQUEST})
        else:
            error_data = {
                "error": True,
                "message": 'Email can not be blank.',
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)


class PasswordResetOtpView(GenericAPIView):
    """
    Password reset otp is verified, therefore
    this resets the user's password.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordResetOtpSerializer
    permission_classes = (AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetOtpView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        custom_data = {
            "error": False,
            "status_code": status.HTTP_200_OK,
            "message": "Password has been reset with the new password.",
            "data": {}
        }
        return Response(custom_data)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data
            login(request, user)
            token = Token.objects.get(user=user)
            return Response({
                "error": False,
                "status_code": status.HTTP_200_OK,
                "message": "Login Successfully",
                "data": UserSerializer(user).data,
                "token": str(token)
            })
        except Exception as e:
            return Response({
                "error": True,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": e,
                "data": {}
            })


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserDetailsSerializer

    def get(self, request, format=None):
        user_data = User.objects.get(id=self.request.user.id)
        serializer = UserDetailsSerializer(user_data)
        custom_data = {
            "error": False,
            "status_code": status.HTTP_200_OK,
            "message": "Profile Details",
            "data": serializer.data
        }
        return Response(custom_data)

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            instance = User.objects.get(pk=self.request.user.id)
            serializer = UserDetailsSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                custom_data = {
                    "error": False,
                    "status_code": status.HTTP_200_OK,
                    "message": "Profile Details Updated",
                    "data": serializer.data
                }
                return Response(custom_data)
            error_data = {
                "error": True,
                "message": serializer.errors,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "data": {}
            }
            return Response(error_data)

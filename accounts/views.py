from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from accounts.serializers import OtpSerializer, PasswordResetOtpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.core.mail import send_mail
from go_fit.settings import DEFAULT_FROM_EMAIL, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from accounts.models import Otp

User = get_user_model()

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class SendOtpApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email', '')
        mobile = request.data.get('mobile', '')

        if email != '':
            user = User.objects.get(email=email)
            otp = random.randint(1000, 9999)
            serializer = OtpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(otp=otp)
            subject = 'LocalMingle Forgot Password Otp'
            message = f"Hello {user.first_name} {user.last_name} \n Your Forgot Password Otp is {otp}"
            try:
                send_mail(subject=subject, message=message, from_email=DEFAULT_FROM_EMAIL, recipient_list=[email],
                          fail_silently=True)
            except:
                return Response({'message': 'Email not send'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'An otp has been sent to your email'}, status=status.HTTP_200_OK)
        elif mobile != '':
            user = User.objects.get(email=mobile)
            otp = random.randint(1000, 9999)
            serializer = OtpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(otp=otp)
            title = 'LocalMingle Forgot Password Otp'
            body = f"Hello {user.first_name} {user.last_name} \n Your Forgot Password Otp is {otp}"

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = TWILIO_ACCOUNT_SID
            auth_token = TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            try:
                message = client.messages.create(body=body,
                                                 from_='+13237451893',
                                                 to='+91' + mobile)
                print(message.sid)
            except:
                return Response({'message': 'Sms not send'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'An otp has been sent to your mobile'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Email or Mobile can not be blank.'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email', '')
        mobile = request.data.get('mobile', '')
        if email != '':
            otp_obj = Otp.objects.get(email=request.data['email'], verify=False)
            if otp_obj:
                if int(request.data['otp']) == otp_obj.otp:
                    serializer = OtpSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    otp_obj.verify = True
                    otp_obj.save()
                    return Response({'message': 'Your otp is verified successfully', 'status': status.HTTP_200_OK})
                else:
                    return Response({'message': 'You have entered wrong otp.', 'status': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'message': 'Please enter valid email to verify otp',
                                 'status': status.HTTP_400_BAD_REQUEST})
        elif mobile != '':
            otp_obj = Otp.objects.get(email=request.data['mobile'], verify=False)
            if otp_obj:
                if int(request.data['otp']) == otp_obj.otp:
                    serializer = OtpSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    otp_obj.verify = True
                    otp_obj.save()
                    return Response({'message': 'Your otp is verified successfully', 'status': status.HTTP_200_OK})
                else:
                    return Response({'message': 'You have entered wrong otp.', 'status': status.HTTP_400_BAD_REQUEST})
            else:
                return Response({'message': 'Please enter valid mobile number to verify otp',
                                 'status': status.HTTP_400_BAD_REQUEST})

        else:
            return Response({'message': 'Email or Mobile can not be blank.'}, status=status.HTTP_400_BAD_REQUEST)


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
        return Response(
            {"detail": "Password has been reset with the new password."}
        )
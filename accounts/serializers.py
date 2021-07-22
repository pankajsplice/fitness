from django.contrib.auth import get_user_model, authenticate
from django.db.models import DateTimeField
from django.utils.timezone import now
from rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer
from rest_framework import serializers
from accounts.models import STAFF_TYPE, Otp
from accounts.models import UserProfile
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm

User = get_user_model()


class RegisterSerializer(DefaultRegisterSerializer):
    """

    """
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    mobile = serializers.CharField(max_length=15)
    type = serializers.ChoiceField(choices=STAFF_TYPE)
    profile_pic = serializers.ImageField(required=False, allow_null=True)

    def custom_signup(self, request, user):
        mobile = self.validated_data.get('mobile', '')
        type = self.validated_data.get('type', '')
        profile_pic = self.validated_data.get('profile_pic', '')
        user_profile = UserProfile(
            user=user,
            mobile=mobile,
            type=type,
            profile_pic=profile_pic,
        )
        user_profile.save()

    def get_cleaned_data(self):
        if settings.USERNAME == 'email':
            username = self.validated_data.get('email', '')
        else:
            username = self.validated_data.get('mobile', '')
        return {
            'username': username,
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'mobile': self.validated_data.get('mobile', ''),
            'type': self.validated_data.get('type', ''),
            'profile_pic': self.validated_data.get('profile_pic', '')
        }


class UserProfileSerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = UserProfile
        fields = ('mobile', 'type', 'profile_pic')


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    profile = UserProfileSerializer()
    last_login = serializers.DateTimeField(default=now(), read_only=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile = validated_data.get('profile')

        if profile:
            profile_obj = UserProfile.objects.get(user__id=instance.pk)
            profile_obj.profile_pic = profile.get('profile_pic', profile_obj.profile_pic)
            profile_obj.mobile = profile.get('mobile', profile_obj.mobile)

            profile_obj.save()
        return instance

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'profile', 'last_login')
        read_only_fields = ('email', )


class OtpSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Otp
        fields = '__all__'


class PasswordResetOtpSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset otp.
    """
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    email = serializers.CharField()

    set_password_form_class = SetPasswordForm

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}
        self.user = User._default_manager.get(email=attrs['email'])
        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self):
        return self.set_password_form.save()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name')

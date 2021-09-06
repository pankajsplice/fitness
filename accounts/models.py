# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.contrib.auth import get_user_model
from django.db import models

from utils.models import ModelMixin

User = get_user_model()

USER_LANGUAGE = (
        ('EN', 'ENGLISH'),
        ('HI', 'हिंदी '),
    )

STAFF_TYPE = (
        ('1', _('Company Admin')),
        ('2', _('Branch Admin')),
        ('3', _('Filed Executive')),
    )

GENDER_TYPE = (
    ('male', 'male'),
    ('female', 'female'),
    ('others', 'others')
)


class UserProfile(models.Model):
    """
    User Profile model store the basic user information
    """
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    # type = models.CharField(max_length=30, choices=STAFF_TYPE, blank=True, null=True)
    step_goal = models.PositiveIntegerField(default=0, blank=True, null=True)
    sleep_goal = models.TimeField(blank=True, null=True)
    mobile = models.CharField(max_length=15, db_index=True, null=True, blank=True)
    nick_name = models.CharField(max_length=100, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_TYPE, null=True, blank=True)
    profile_pic = models.ImageField(blank=True, null=True, help_text=_('Upload your profile pic'))


class Otp(models.Model):
    email = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    otp = models.IntegerField(blank=True)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.email

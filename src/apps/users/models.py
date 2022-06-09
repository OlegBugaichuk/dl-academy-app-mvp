from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Types(models.IntegerChoices):
    OWNER = 1
    LECTOR = 2
    MENTOR = 3
    STUDENT = 4


class CustomUser(AbstractUser):
    patronomyc = models.CharField(_("patronomyc"), max_length=150, blank=True)
    type = models.IntegerField(choices=Types.choices, default=Types.STUDENT)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Types(models.IntegerChoices):
    OWNER = 1
    LECTOR = 2
    MENTOR = 3
    STUDENT = 4


class CustomUser(AbstractUser):
    patronomyc = models.CharField(_("patronomyc"), max_length=150, blank=True)
    type = models.IntegerField(choices=Types.choices, default=Types.STUDENT)
    edu_groups = models.ManyToManyField("users.Group", 
                                        related_name="students", 
                                        blank=True, null=True)


class UserMentorRel(models.Model):
    student = models.OneToOneField(CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name='mentor_rel')

    mentor = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='students')


class Group(models.Model):
    number = models.CharField(_("number"), max_length=5)
    lector = models.ForeignKey(CustomUser,
                               null=True,
                               on_delete=models.SET_NULL,                               
                               related_name='lector_groups')

    course = models.ForeignKey("courses.Course",
                               on_delete=models.CASCADE,
                               related_name='groups')
    
    def __str__(self):
        return self.number
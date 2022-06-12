from calendar import c
from django.db import models
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextField


class CoursesAbstract(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.CharField(_('description'),
                                   max_length=150,
                                   blank=True)
    
    class Meta:
        abstract = True


class Course(CoursesAbstract):
    def __str__(self):
        return self.title

class Module(CoursesAbstract):
    courses = models.ManyToManyField(Course, related_name='modules')

    def __str__(self):
        return self.title


class Lection(CoursesAbstract):
    content = MDTextField()
    modules = models.ManyToManyField(Module, related_name='lections')

    def __str__(self):
        return self.title
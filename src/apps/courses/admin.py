from django.contrib import admin
from .models import Course, Module, Lection


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Lection)
class LectionAdmin(admin.ModelAdmin):
    pass
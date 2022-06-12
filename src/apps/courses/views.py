from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .models import Course, Module, Lection
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexView(View):

    @login_required
    def get(self, request, *args, **kwargs):
        user = request.user
        user_edu_groups = user.edu_groups.all()
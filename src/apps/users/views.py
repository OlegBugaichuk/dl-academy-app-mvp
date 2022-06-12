from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from .forms import SignUpForm
from .models import Types


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        # if user.type != Types.OWNER:
        #     return Http404()
        
        return super().get(request, *args, **kwargs)
    
        
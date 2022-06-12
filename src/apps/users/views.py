from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import Http404
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Types


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('admin:index')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.type != Types.OWNER:
            raise Http404()
        
        return super().get(request, *args, **kwargs)
    
        
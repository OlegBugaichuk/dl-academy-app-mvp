from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.utils.decorators import method_decorator
from django.http.response import Http404
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm
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
    

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.type != Types.OWNER:
            raise Http404()

        form = self.form_class(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
        return redirect(self.success_url)
        
        
class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
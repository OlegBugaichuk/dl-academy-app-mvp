from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, 
                                       UsernameField)
from django.contrib.auth import get_user_model, password_validation
from django import forms
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class CustomCheckBoxWidget(forms.CheckboxSelectMultiple):
    option_template_name = 'core/widgets/checkbox_option.html'


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Пароль"
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "placeholder": "Подтвердить пароль"
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'patronomyc',
            'type', 'edu_groups'
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': _('Логин')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Email')}),
            'first_name': forms.TextInput(attrs={'placeholder': _('Имя')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Фамилия')}),
            'patronomyc': forms.TextInput(attrs={'placeholder': _('Отчество')}),
            'type': forms.Select(attrs={'placeholder': _('Тип аккаунта')}),
            'edu_groups': CustomCheckBoxWidget(
                attrs={'placeholder': _('Группа обучения')}
            )
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True, 
        "class": "form-control",
        "placeholder": "Имя пользователя"
    }))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "class": "form-control",
            "placeholder": "Пароль"
        }),
    )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'patronomyc',
            'type', 'edu_groups'
        )
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'usernickname',
            'email',
            'password1',
            'password2'
        )
        labels = {
            'usernickname': 'Имя пользователя',
            'email': 'Электронная почта',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }

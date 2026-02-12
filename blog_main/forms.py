from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# UserCreationForm used to create a user as in the admin panel


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

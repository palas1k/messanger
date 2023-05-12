from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = 'username', 'email'
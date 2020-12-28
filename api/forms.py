from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import userProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = userProfile
        fields = ('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = userProfile
        fields = ('email',)
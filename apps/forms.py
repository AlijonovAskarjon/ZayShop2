from django.forms import ModelForm

from apps.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'password',
            'username',
            'email',
            'phone_number'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        return user


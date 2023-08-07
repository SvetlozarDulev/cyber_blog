from django import forms
from django.contrib.auth.models import Group

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('staff', 'Guest'),
        ('superuser', 'Writer'),
    ])
    class Meta:
        model = CustomUser
        fields = ("username", "email", "years_experience", 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']

        if commit:
            user.save()

        if role == 'staff':
            user.is_staff = True
            staff_group = Group.objects.get(name='guest')
            user.groups.add(staff_group)
        elif role == 'superuser':
            user.is_superuser = True
            write_group = Group.objects.get(name='writer')
            user.groups.add(write_group)

        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "years_experience")




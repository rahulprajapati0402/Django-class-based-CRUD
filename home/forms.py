from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {
            "password": forms.PasswordInput(
                render_value=True,
                attrs={"class": "form-control", "placeholder": "Enter password"},
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter first name", "class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Enter last name", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter email", "class": "form-control"}
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "Enter username", "class": "form-control"}
            ),
        }

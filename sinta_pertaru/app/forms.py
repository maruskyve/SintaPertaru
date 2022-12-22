from django import forms
from . import models


class UserForm(forms.ModelForm):
    # Optional required field
    user_phone_number = forms.CharField(required=False)
    user_email = forms.CharField(required=False)

    class Meta:
        model = models.User
        fields = "__all__"


class LSDataForm(forms.ModelForm):
    class Meta:
        model = models.LandData
        fields = "__all__"


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = models.GuestBook
        fields = "__all__"

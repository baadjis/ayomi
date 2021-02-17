from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile


class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = [

            'email',

            'bio'

        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()

        bio = cleaned_data.get("bio")

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )

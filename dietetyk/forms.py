import django.forms as forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from dietetyk.models import Note


class LoginForm(forms.Form):
    """Login details form"""
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


def validate_username_is_not_taken(value):
    """Login unique check function"""
    users = User.objects.filter(username=value)
    if len(users) > 0:
        raise ValidationError("Zogin zajety")


class RegisterForm(forms.Form):
    """User register form"""
    username = forms.CharField(label='Nazwa użytkownika', max_length=50, validators=[validate_username_is_not_taken])
    pass1 = forms.CharField(label='hasło', max_length=50, widget=forms.PasswordInput)
    pass2 = forms.CharField(label="powtórz hasło", max_length=50, widget=forms.PasswordInput)
    first_name = forms.CharField(label="imię", max_length=50)
    last_name = forms.CharField(label='nazwisko', max_length=50)
    email = forms.EmailField(label='email', max_length=50)

    def clean(self):
        """function used to check if passwords are the same"""
        cleaned_data = super().clean()
        if cleaned_data['pass1'] != cleaned_data['pass2']:
            raise ValidationError("Hasła nie są takie same!")
        return cleaned_data

class NoteAddForm(forms.ModelForm):
    """New note add form"""

    class Meta:
        model = Note
        fields = '__all__'
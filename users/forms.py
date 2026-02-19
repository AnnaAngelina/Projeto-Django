from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         labels = {'username': 'nome', 'password': 'senha'}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput())

    def clean_username(self):
        nome = self.cleaned_data['username']
        if not(nome.isalnum()):
            raise ValidationError('O nome de usuário não deve conter caracteres especiais')
        return nome

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from .models import MyUser
from django_recaptcha.fields import ReCaptchaField


class UserCreationForm(forms.ModelForm):
    recaptcha = ReCaptchaField()

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    code_word = forms.CharField(label='Кодовое слово',
                                widget=forms.TextInput(attrs={'placeholder': 'Введите кодовое слово'}))

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'recaptcha')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def clean_code_word(self):
        code_word = self.cleaned_data.get('code_word')
        if code_word != 'arnbbErTbUla':
            raise forms.ValidationError("Неверное кодовое слово")
        return code_word

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    recaptcha = ReCaptchaField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'recaptcha')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))

    def confirm_login_allowed(self, user):
        # Если требуется дополнительная проверка при аутентификации
        if not user.is_active:
            raise forms.ValidationError(
                "Этот аккаунт не активен.",
                code='inactive',
            )

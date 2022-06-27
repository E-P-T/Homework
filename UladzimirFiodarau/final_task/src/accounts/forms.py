from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()
        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('User not registered')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Incorrect password')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Account is deactivated')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label='Please, input your email',
                            widget=forms.EmailInput(attrs={'class': 'form-control'})
                            )
    password = forms.CharField(label='Please, input password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               )
    password2 = forms.CharField(label='Please, repeat password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return data['password2']


class UserUpdateForm(forms.Form):
    send_email = forms.BooleanField(required=False,
                                    widget=forms.CheckboxInput,
                                    label='Sending email notifications')

    class Meta:
        model = User
        fields = ('send_email', )

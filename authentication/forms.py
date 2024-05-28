from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class LoginForm(forms.Form):
        
        username = forms.CharField(max_length=30)
        password = forms.CharField(widget=forms.PasswordInput)
        
class RegisterForm(UserCreationForm):
        
        class Meta(UserCreationForm.Meta):
                model = User
                fields = ['username', 'first_name', 'last_name', 'email', 'profil_photo', 'birthday', 'role']
                widgets = {
			'birthday' : forms.DateInput(attrs={'type' : 'date'})
		}
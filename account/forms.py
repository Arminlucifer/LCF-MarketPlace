from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({'placeholder':field.label})
            field.widget.attrs.update({'name': field.label})

        if 'email' in self.fields:
             self.fields['email'].widget.attrs.update({'placeholder':"example@gmail.com"})
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder':"Enter Your Username"})
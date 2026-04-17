from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import User

class MyUserCreationForm(UserCreationForm):


    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    avatar = forms.ImageField(required=False)


    class Meta:
        model = User

        fields = ['name', 'username', 'email', 'password1', 'password2', 'avatar']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        bootstrap_class = 'form-control'
        floating_class = 'form-floating'

        for field_name, field in self.fields.items():

            field.widget.attrs.update({'class': bootstrap_class})


            if field_name not in ['password', 'password_confirm']:

                field.widget.attrs.update({'placeholder': field.label})


            if field_name == 'password':
                field.widget.attrs.update({'placeholder': "Enter Your Password"})
            elif field_name == 'password_confirm':
                 field.widget.attrs.update({'placeholder': "Confirm Your Password"})



        if 'email' in self.fields:
             self.fields['email'].widget.attrs.update({'placeholder':"example@gmail.com"})


        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder':"Enter Your Username"})


        for field_name, field in self.fields.items():

             if 'placeholder' in field.widget.attrs:
                 del field.widget.attrs['placeholder']

             field.widget.attrs.update({'class': bootstrap_class})


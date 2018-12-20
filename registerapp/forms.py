from django import forms
from multiselectfield import MultiSelectFormField
from .porter import *
from django.contrib.auth import get_user_model
from .models import RegistrationData



User = get_user_model()

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = RegistrationData
        fields = '__all__'



    # username = forms.CharField(
    #     label= 'username' ,
    #     widget= forms.TextInput(
    #
    #         attrs= {
    #             'class':'form-control',
    #             'place-holder':'usename'
    #
    #         }
    #
    #     )
    #
    # )
    # email = forms.EmailField(
    #
    #     label= 'email',
    #     widget= forms.EmailInput(
    #
    #         attrs={
    #             'class': 'form-control',
    #             'place-holder': 'email'
    #
    #         }
    #
    #     )
    # )
    # upassword = forms.CharField(
    #
    #     label = 'password',
    #     widget = forms.PasswordInput(
    #
    #         attrs= {
    #             'class':'form-control' ,
    #             'place-holder' :'password'
    #
    #         }
    #     )
    # )
    # upassword2 = forms.CharField(
    #
    #     label='re-enter password',
    #     widget=forms.PasswordInput(
    #
    #         attrs={
    #             'class': 'form-control',
    #             'place-holder': 'password'
    #
    #         }
    #     )
    # )
    #
    # dob = forms.DateField(
    #
    #     widget= forms.SelectDateWidget(
    #
    #         years=YEARS
    #
    #     )
    #
    # )
    #
    # location  = MultiSelectFormField(
    #
    #   choices= LOCATION_CHOICES
    # )
    #
    # gender = forms.ChoiceField(
    #
    #     widget= forms.RadioSelect ,
    #     choices= GENDER_CHOICES
    # )

    # def clean_username(self):
    #     print('cleaned data',self.cleaned_data)
    #     username = self.cleaned_data.get('username')
    #     us = RegistrationData.objects.filter(username=username)
    #     print(us)
    #     print('user name validating reg form' + str(us))
    #     if us:
    #         raise forms.ValidationError('user name is taken')
    #     return username
    # def clean_dob(self):
    #     dob = self.cleaned_data.get('dob')
    #     print(dob)
    #     if dob is None:
    #         raise forms.ValidationError('enter dob')
    #     return self.cleaned_data.get('dob')
    # def clean(self):
    #     upassword = self.cleaned_data.get('upassword')
    #     upassword2 = self.cleaned_data.get('upassword2')
    #     if upassword!= upassword2 :
    #         raise forms.ValidationError('password not matching')
    #     return upassword

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     es = User.objects.filter(email=email)
    #     if es.exists():
    #         raise forms.ValidationError('email is taken')
    #     elif not '@gmail.com' in email:
    #         raise forms.ValidationError('please enter complete email !')
    #     return email
    # def clean_location(self):
    #     location = self.cleaned_data.get('location')
    #     if is_empty(location):
    #         raise forms.ValidationError('please enter location')
    #     return location

    # def clean_gender(self):
    #     gender = self.cleaned_data.get('gender')
    #     if is_empty(gender):
    #         raise forms.ValidationError('please enter location')
    #     return gender


class LoginForm(forms.Form):

    username = forms.CharField(
        label= 'username' ,
        widget= forms.TextInput(

            attrs= {
                'class':'form-control',
                'place-holder':'usename'

            }

        )

    )
    upassword = forms.CharField(

        label = 'password',
        widget = forms.PasswordInput(

            attrs= {
                'class':'form-control' ,
                'place-holder' :'password'

            }
        )
    )
    def clean_username(self):
        print(self.cleaned_data)
        username = self.cleaned_data.get('username')
        us = RegistrationData.objects.filter(username=username)
        print('user name validating' + str(us))
        if  is_empty(us):
            raise forms.ValidationError('username does not exist')
        return username



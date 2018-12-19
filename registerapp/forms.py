from django import forms
from multiselectfield import MultiSelectFormField
from .porter import *

class RegistrationForm(forms.Form):

    username = forms.CharField(
        label= 'username' ,
        widget= forms.TextInput(

            attrs= {
                'class':'form-control',
                'place-holder':'usename'

            }

        )

    )
    email = forms.EmailField(

        label= 'email',
        widget= forms.EmailInput(

            attrs={
                'class': 'form-control',
                'place-holder': 'email'

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

    dob = forms.DateField(

        widget= forms.SelectDateWidget(

            years=YEARS

        )

    )

    location  = MultiSelectFormField(

      choices= LOCATION_CHOICES
    )

    gender = forms.ChoiceField(

        widget= forms.RadioSelect ,
        choices= GENDER_CHOICES
    )



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



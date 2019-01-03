from django.shortcuts import render , redirect
from .forms import RegistrationForm ,LoginForm
from .models import RegistrationData
from django.http import HttpRequest , HttpResponse
from .passwordhash import *
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()


def registrationview(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            username = request.POST.get('username' ,'')
            email = request.POST.get('email', '')
            upassword = request.POST.get('upassword', '')
            # dob = request.POST.get('dob','')

            location = request.POST.get('location', '')
            gender  = request.POST.get('gender','')
            data = RegistrationData(
                username= username,
                upassword= hasher(upassword),
                email= email ,
                location=location,
                gender = gender
            )
            data.save()
            return redirect('/')
        return render(request, 'registration.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration.html', context)


def loginview(request):
    hash = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username' ,'')
            upassword = request.POST.get('upassword', '')

            un = RegistrationData.objects.filter(username=username)
            hash = RegistrationData.objects.values('upassword')
            if un :
              if  (checker(hash,upassword) == True)  :
                  return redirect('/home/')
            return redirect('/')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:

        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def homeview(request):
    return None
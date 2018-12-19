from django.shortcuts import render , redirect
from .forms import RegistrationForm ,LoginForm
from .models import RegistrationData
from django.http import HttpRequest , HttpResponse
from .passwordhash import *

# Create your views here.


def registrationview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username' ,'')
            email = request.POST.get('email', '')
            upassword = request.POST.get('upassword', '')
            dob = form.cleaned_data.get('dob','')
            location = form.cleaned_data.get('location', '')
            gender  = form.cleaned_data.get('gender','')
            data = RegistrationData(
                username=username ,
                email= email,
                upassword= hasher(upassword) ,
                dob=dob,
                location=location ,
                gender=gender
            )
            data.save()
            # form = RegistrationForm()
            return  redirect('/')
        # return render(request , 'registration.html',{'form': form})
    else:

        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})



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
                  return HttpResponse('Invalid')
            form = LoginForm()
            return render(request , 'login.html',{'form': form})
    else:

        form = LoginForm()
        return render(request, 'login.html', {'form': form})









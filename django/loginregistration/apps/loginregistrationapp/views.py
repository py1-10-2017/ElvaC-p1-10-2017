from django.shortcuts import render, HttpResponse,redirect
from .models import userinfo
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA_REGEX = re.compile(r'^[A-Za-z]+$')


def index(request):
    return render(request, "loginregistrationapp/index.html")

##### LOGIN REGISTRATION PROCESS #####
def newregister(request):
    nologinerrors = True

    if len(request.POST['first_name']) < 2:
        messages.add_message(request, messages.ERROR, "Your first name is too short")
        nologinerrors = False

    if len(request.POST['last_name']) < 2:
        messages.add_message(request, messages.ERROR, "Your last name is too short")
        nologinerrors = False

    if not ALPHA_REGEX.match(request.POST['last_name']):
        messages.add_message(request, messages.ERROR, "Your last name contains number")
        nologinerrors = False

    if not ALPHA_REGEX.match(request.POST['first_name']):
        messages.add_message(request, messages.ERROR, "Your first name contains a number")
        nologinerrors = False

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request, messages.ERROR, "Your email is not in a valid format")
        notloginerrors = False

    if request.POST['password'] < 8:
        messages.add_message(request, messages.ERROR, "your password is too short")
        nologinerrors = False

    if request.POST['password'] != request.POST['confirmpassword']:
        messages.add_message(request, messages.ERROR, "your passwords don't match")
        nologinerrors = False

    if nologinerrors == False:
        return redirect ('/')

    else :
        userinfo.objects.newregister(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'])

        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        return render(request,"loginregistrationapp/successpage.html" )

##### LOGIN REGISTRATION PROCESS #####
def loginregister(request):
    email = request.POST['Email']
    password = request.POST['Password']

    if userinfo.objects.unencrypt(email, password):
        return render(request,"loginregistrationapp/successpage.html")
    else:
        messages.add_message(request, messages.ERROR, "invalid login or password")
        return redirect('/')

##### CLEAR SESSION PROCESS #####
def clearregister(request):
    request.session.clear
    return redirect('/')

# Create your views here.

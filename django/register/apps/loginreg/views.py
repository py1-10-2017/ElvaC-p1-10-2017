from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.
def index(req):
    return render(req, "loginreg/index.html")
def login(req):
    #return HttpResponse("got to login")
    result =  User.objects.validate(req.POST)
    if result[0]:
        #go look in database
        user = User.objects.filter(email=req.POST["email"])
        if len(user) > 0:
            #user exist check password
            user = user[0]
            if bcrypt.checkpw(req.POST["password"].encode(), user.password.encode()):
                req.session["user_id"] = user.id
                req.session["email"] = user.email
                #messages.error(req, "Your in but my app doesnt do anything yet")
                return render(req, "loginreg/success.html")
            else:
                messages.error(req, "password do not match")
        else:
            messages.error(req, "email does not exist")
        return redirect("/loginreg")
        #returns TRUE validation is passed
        #create User
    else:
        #grab errors
        errors =  result[1]
        for error in errors:
            messages.error(req, error)
        return redirect('/loginreg')
def register(req):
    #return HttpResponse("got to registration")
    result =  User.objects.validate(req.POST) #tuple True/False and error message
    if result[0]:
        hashed_pw = bcrypt.hashpw(req.POST["password"].encode(), bcrypt.gensalt())
        User.objects.create(email=req.POST["email"], password=hashed_pw)
        messages.error(req, "Registration Successful")
        return redirect("/loginreg")
        #returns TRUE validation is passed
        #create User
    else:
        #grab errors
        errors =  result[1]
        for error in errors:
            messages.error(req, error)
        return redirect('/loginreg')
        #pass to view
def success(request):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    return render(request, 'loginReg/success.html')
def logout(request):
    request.session.pop('user_id')
    return redirect(reverse('index'))

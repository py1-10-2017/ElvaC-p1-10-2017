from django.shortcuts import render, redirect
from .models import Course_registration


#GO TO INDEX PAGE AND GRAB ALL OF THE DATA FROM THE COURSE REGISTRATION CLASS
def index(request):
    context = {
    "courseregistration" : Course_registration.objects.all()
    }
    return render (request, "courses_app/index.html", context)

#REDIRECT BACK TO INDEX PAGE AFTER CREATING A NEW COURSE
def course_addon(request):
    Course_registration.objects.create(course_name = request.POST['coursename'], description = request.POST['description'])
    return redirect ('/')

#GO TO DELETE PAGE FOR DELETING A COURSE
def delete(request, id):
    course = Course_registration.objects.filter(id = id)
    context = {
    "specificcourse" : course
    }
    return render (request, 'courses_app/delete.html', context)

#DELETE CONFIRMATION
def delconfirmation(request, id):
    x = 100
    Course_registration.objects.filter(id=id).delete()
    print Course_registration.objects.square(x)
    return redirect('/')

#GO BACK TO INDEX PAGE & DO NOT DELETE RECORD
def no_delete(request):
    return redirect('/')

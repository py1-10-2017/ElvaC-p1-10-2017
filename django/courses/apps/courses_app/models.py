# from __future__ import unicode_literals
from django.db import models

class Course_registration_manager(models.Manager):
    def test(self):
        print "///////////////////////////////////"
        
    # def create_course(self, course_name, description):
    #     try:
    #         return Course_registration.objects.get(course_name = course_name)
    #
    #     except:
    #         return Course_registration.objects.create(course_name = course_name, description = description)

    def square(self, x):
        return x * x


class Course_registration(models.Model):
    course_name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    ##SETTING OBJECTS...
    objects = Course_registration_manager()

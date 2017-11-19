from __future__ import unicode_literals
from django.db import models
import bcrypt

class userinfomanager(models.Manager):
    def newregister(self, first_name, last_name, email, password):
        hashpw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        userinfo.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashpw)

    def unencrypt(self, email, password):
        try:
            user = userinfo.objects.get(email = email)
            hashpw = bcrypt.hashpw(password.encode(), user.password.encode())
            if hashpw == user.password :
                return True
            else:
                return False
        except:
            return False

class userinfo (models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    objects = userinfomanager()

# Create your models here.

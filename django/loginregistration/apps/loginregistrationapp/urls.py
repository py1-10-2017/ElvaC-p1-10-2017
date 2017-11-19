from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^newregister$',newregister),
    url(r'^loginregister$',loginregister),
    url(r'^clearregister$',clearregister)
]

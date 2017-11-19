from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^course_addon$', course_addon),
    url(r'^delete/(?P<id>\d+)$', delete),
    url(r'^deleteconfirmation/(?P<id>\d+)$',delconfirmation),
    url(r'^noDelete$', no_delete)
]

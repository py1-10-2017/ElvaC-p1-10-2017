# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "this is the home page"
    return HttpResponse(response)
def books(request):
    response = "this is theh book page"
    return HttpResponse(response)

def authors(request):
    response = "this is theh author page"
    return HttpResponse(response)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext, Template
import datetime

# Create your views here.
def index(request):

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    s = "hello"
    s2 = [1,22,333]
    s3 = {"username":"alex", "sex":"male"}
    s4 = datetime.datetime.now()
    s5 = Person("yuan", 18)
    s6 = 6
    s7 = [111,222]
    s8 = "<a href='#'>jump</a>"
    s9 = ""

    # return render(request, "index.html", {"obj":s3})
    return render(request, "index.html", {"obj": s8})
    # return render(request, "index.html")

def login(request):
    if request.method=="POST":
        return HttpResponse("OK")
    name = "hello"
    num = 1200
    # return render(request, "login.html", locals())

    return render(request, "login.html", locals())
    # have a little bug. add .context_instance=RequestContext(request)
    # return render_to_response("login.html", locals(), content_type=RequestContext(request))

def ordered(request):
    return render(request, "ordered.html")

def shopping_cart(request):
    return render(request, "shopping_cart.html")
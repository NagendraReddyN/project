from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstfun(request):
    resp=HttpResponse("Good evening guys")

    return resp

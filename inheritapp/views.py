from django.shortcuts import render
from django.http import HttpResponse


def homepage2(request):
    return HttpResponse('inheritapp has been called')

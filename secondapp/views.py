from django.shortcuts import render
from django.http import HttpResponse

def secondfun(request):

    #resp=HttpResponse("This is Django server response")

    return render(request,'second.html')

# Create your views here.

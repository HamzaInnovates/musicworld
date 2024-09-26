from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def bollywood(request):
    return render(request,'bollywood.html')
def ncs(request):
    return render(request,'ncs.html' )
def pop(request):
    return render(request,'pop.html' )

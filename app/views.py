from django.shortcuts import render

from django.urls import path

def one(request):
    return render(request,'one.html')
def two(request):
    return render(request,'two.html')
def three(request):
    return render(request,'three.html')
def five(request):
    return render(request,'five.html')

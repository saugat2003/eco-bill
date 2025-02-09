from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def receipt(request):
    return render(request, 'base/receipt.html')

def org_add(request):
    return render(request, 'base/org_add.html')

def signup(request):
    return render(request, 'base/signup.html')
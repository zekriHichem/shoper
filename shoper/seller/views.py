from django.shortcuts import render

# Create your views here.


def login_page(request):
    return render(request,'registration/login.html')

def signup_page(request):
    return render(request,'registration/signup.html')

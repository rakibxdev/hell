from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render (request, 'home.html')


def login(request):
    if request.method=='POST':
        mail = request.POST["mail"]
        passw = request.POST["pass"]
        print(f"mail:{mail}\nPassword: {passw}")
    else:
        print("no post")
    return render (request, 'signin.html')



def sign(request):
   if request.method=='POST':
        username = request.POST.get("name")
        mail = request.POST.get("mail")
        passw = request.POST.get("password")
        print(f"User:{username}\nmail {mail}\nPassword: {passw}")
   return render (request, 'signup.html')

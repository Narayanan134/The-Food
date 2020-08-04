from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        Emailid=request.POST['email']
        password=request.POST['password']
        ConfirmPassword=request.POST['cp']
        
        if password==ConfirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect("signup")
            elif(User.objects.filter(email=Emailid).exists()):
                messages.info(request,"Email taken")
                return redirect("signup")
            else:
                user=User.objects.create_user(username=username,password=password,email=Emailid,first_name=firstname,last_name=lastname)
                user.save()
                print("User created")
                return redirect("login")
        else:
            print("Password not matching")
            return redirect("signup")
        return redirect("home.html")
    else:
        return render(request,"signup.html")

    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("login")
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("/")
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import User_Profile
from .forms import User_Account, Profile_Form
from django.contrib.auth import password_validation

from django.contrib.auth import login,logout,authenticate

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def account(request):
    return render(request, 'omsaccount/account.html')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profiles')

        else:
            messages.error(request, "Password or Username is incorrect")

    return render(request, 'omsaccount/login.html')
def page(request):
    a = User_Profile.objects.all()
    return render(request, "omsaccount/page.html", {'a':a})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('login')

    
def register(request):
    a = User_Account()
    if request.method == "POST":
        a = User_Account(request.POST, request.FILES)
        if a.is_valid():
            user = a.save(commit=False)
            user.save()

            messages.success(request, "Your account has been successfully created")

            login(request,user)
            return redirect('user_profiles')
        else:
            messages.error(request, "an error has occured during registration.\n Please Try again")

    return render(request, 'omsaccount/register.html', {'a':a})

def user_profiles(request):
    a = User_Profile.objects.all()
    return render(request,'omsaccount/user_profiles.html',{'a':a})

def prof(request):
    a = Profile_Form()
    if request.method == "POST":
        a = Profile_Form(request.POST)
        if a.is_valid():
            a.save()
            return redirect("user_profiles")
    return render(request, "omsaccount/prof.html", {'a':a})

def edit_profile(request, pk):
    b = User_Profile.objects.get(id = pk)
    a = Profile_Form(instance=b)
    if request.method == "POST":
        a = Profile_Form(request.POST, request.FILES, instance=b)
        if a.is_valid():
            a.save()
            return redirect('user_profiles')
    return render(request, "omsaccount/prof.html", {'a':a} )

def delete_profile(request, pk):
    a = User_Profile.objects.get(id=pk)
    a.delete()
    return redirect('user_profiles')

def profile(request,pk):
    a = User_Profile.objects.get(id = pk)
    return render(request, 'omsaccount/profile.html', {'a':a})
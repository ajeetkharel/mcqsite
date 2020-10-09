from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.user.is_authenticated:
        return redirect('exam-home')
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('exam-home')
            else:
                print("Failed")
        return render(request, 'user/login.html')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('exam-home')
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                email = request.POST["email"]
                password = request.POST["password1"]
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('exam-home')
                else:
                    print("Registration failed")
            return render(request, 'user/register.html', context={'form':form})
    return render(request, 'user/register.html')
    
def logout_user(request):
    logout(request)
    return redirect('user-login')
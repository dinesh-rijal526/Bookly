from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username = username, password = password)
        print(username)
        print(password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Your Username or Password Does't Match!!")
            return render(request, 'accounts/login.html')
        
    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        username = data.get('username')
        password1 = data.get('password')
        password2 = data.get('confirm-password')

        if password1 != password2:
            messages.error(request, "Enter Same Password In Both Password Field!!")
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "The Email Already Being Used!!")
            return render(request, 'accounts/register.html')
        print(name)
        print(email)
        print(password1)
        try:
            user = User.objects.create_user(
                first_name = name,
                username = username,
                email = email,
                password = password1
            )

            login(request, user)
            return redirect('home')

        except Exception as e:
            messages.error(request, "Something Went Wrong!!")
            return render(request, 'accounts/register.html')
        
    return render(request, 'accounts/register.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')


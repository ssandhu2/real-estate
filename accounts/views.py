from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if(request.method == 'POST'):
        #here register user
        
        #to get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        #validation
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is taken')
                    return redirect('register')
                else: 
                    user = User.objects.create_user(username = username, password= password, email=email, first_name=first_name, last_name=last_name) #put this in user table

                    #below redirect to login to after registering instead of logging in directly 
                    user.save()
                    messages.success(request, 'you are registered')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match') #show error on the front end
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if(request.method == 'POST'):
        #here login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)  #authenticate

        if user is not None: #found in db with the username and password
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if(request.method == 'POST'):
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
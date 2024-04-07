from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})


def home(request):
    return render(request,'home.html', {'userName' : request.user.username})


def my_view(request):
    return render(request, 'login.html', {'csrf_token': request.CSRF_TOKEN})
